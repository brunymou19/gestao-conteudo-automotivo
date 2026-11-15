import os, secrets
from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from app.db import conectar
from app.conteudo import service as conteudo
from app.producao import service as producao
from app.agenda import service as agenda
from app.acesso import service as acesso
from app.eventos_oportunidades import service as eo

def create_app(db_path="conteudo.db", secret_key=None):
    app = Flask(__name__)
    app.secret_key = secret_key or os.environ.get("SECRET_KEY") or secrets.token_hex(32)
    app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")
    conn = conectar(db_path)
    app.config["CONN"] = conn
    conteudo.semear_categorias(conn)
    corpo = lambda: request.get_json(silent=True) or {}

    @app.before_request
    def exigir_login():
        if request.endpoint in ("login", "static") or session.get("usuario_id"):
            return None
        if request.path.startswith("/api/"):
            return jsonify(erro="Não autenticado"), 401
        return redirect(url_for("login"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            uid = acesso.autenticar(conn, request.form.get("usuario"), request.form.get("senha"))
            if uid:
                session.clear(); session["usuario_id"] = uid
                return redirect(url_for("index"))
            return render_template("login.html", erro="Usuário ou senha inválidos"), 401
        return render_template("login.html")

    @app.post("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))

    def erro(e):
        return jsonify(erro=str(e)), (404 if isinstance(e, LookupError) else 400)
    app.register_error_handler(ValueError, erro)
    app.register_error_handler(LookupError, erro)

    @app.get("/")
    def index(): return render_template("index.html")

    # categorias e estados
    @app.get("/api/categorias")
    def cats(): return jsonify(conteudo.listar_categorias(conn))

    @app.post("/api/categorias")
    def nova_cat(): return jsonify(id=conteudo.criar_categoria(conn, corpo().get("nome"))), 201

    @app.get("/api/estados")
    def estados(): return jsonify(producao.ESTADOS)

    # conteúdos e materiais (referências)
    @app.post("/api/conteudos")
    def novo():
        j = corpo()
        return jsonify(id=conteudo.criar_conteudo(conn, j.get("titulo"), j.get("descricao", ""),
                                                   j.get("categoria_id") or None)), 201

    @app.get("/api/conteudos")
    def lista(): return jsonify(conteudo.listar_conteudos(conn, request.args.get("estado")))

    @app.patch("/api/conteudos/<int:cid>/estado")
    def estado(cid):
        producao.mudar_estado(conn, cid, corpo().get("estado")); return jsonify(ok=True)

    @app.get("/api/conteudos/<int:cid>/materiais")
    def materiais(cid): return jsonify(conteudo.listar_materiais(conn, cid))

    @app.post("/api/conteudos/<int:cid>/materiais")
    def novo_material(cid):
        j = corpo()
        return jsonify(id=conteudo.adicionar_material(conn, cid, j.get("tipo"), j.get("referencia"))), 201

    @app.delete("/api/materiais/<int:mid>")
    def del_material(mid):
        conteudo.remover_material(conn, mid); return jsonify(ok=True)

    # agenda
    @app.post("/api/agenda")
    def agendar():
        j = corpo()
        return jsonify(agenda.agendar(conn, j.get("conteudo_id"), j.get("data", ""), j.get("hora", "")))

    @app.patch("/api/agenda/<int:cid>")
    def mover(cid):
        j = corpo()
        return jsonify(agenda.mover(conn, cid, j.get("data", ""), j.get("hora")))

    @app.get("/api/agenda")
    def ver_agenda(): return jsonify(agenda.listar_agenda(conn))

    @app.get("/api/pendentes")
    def pend(): return jsonify(agenda.pendentes(conn))

    @app.get("/api/sugestoes")
    def sugestoes(): return jsonify(agenda.sugestoes(conn, int(request.args.get("dias", 14))))

    @app.get("/api/regras-semanais")
    def regras(): return jsonify(agenda.listar_regras(conn))

    @app.put("/api/regras-semanais")
    def regra():
        j = corpo()
        agenda.definir_regra(conn, j.get("dia_semana"), j.get("descricao"), j.get("categoria_id"))
        return jsonify(ok=True)

    @app.delete("/api/regras-semanais/<int:dia>")
    def del_regra(dia):
        agenda.remover_regra(conn, dia); return jsonify(ok=True)

    # eventos e oportunidades
    @app.get("/api/eventos")
    def eventos(): return jsonify(eo.listar_eventos(conn))

    @app.post("/api/eventos")
    def novo_evento():
        j = corpo()
        return jsonify(id=eo.criar_evento(conn, j.get("nome"), j.get("data"), j.get("solicitante"),
                                          j.get("tipo"), j.get("prazo"))), 201

    @app.patch("/api/eventos/<int:eid>/situacao")
    def evento_situacao(eid):
        eo.mudar_situacao_evento(conn, eid, corpo().get("situacao")); return jsonify(ok=True)

    @app.post("/api/eventos/<int:eid>/agendar")
    def evento_agendar(eid):
        j = corpo()
        return jsonify(eo.agendar_evento(conn, eid, j.get("data", ""), j.get("hora", "")))

    @app.get("/api/oportunidades")
    def oportunidades(): return jsonify(eo.listar_oportunidades(conn))

    @app.post("/api/oportunidades")
    def nova_oportunidade():
        j = corpo()
        return jsonify(id=eo.criar_oportunidade(conn, j.get("contato"), j.get("canal"),
                                                j.get("proposta"), j.get("condicoes", ""))), 201

    @app.patch("/api/oportunidades/<int:oid>/situacao")
    def oportunidade_situacao(oid):
        eo.mudar_situacao_oportunidade(conn, oid, corpo().get("situacao")); return jsonify(ok=True)

    return app
