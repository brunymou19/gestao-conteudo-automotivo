from flask import Flask, jsonify, request, render_template
from app.db import conectar
from app.conteudo import service as conteudo
from app.producao import service as producao
from app.agenda import service as agenda

def create_app(db_path="conteudo.db"):
    app = Flask(__name__)
    conn = conectar(db_path)

    def erro(e):
        return jsonify(erro=str(e)), (404 if isinstance(e, LookupError) else 400)
    app.register_error_handler(ValueError, erro)
    app.register_error_handler(LookupError, erro)

    @app.get("/")
    def index(): return render_template("index.html")

    @app.get("/api/categorias")
    def cats(): return jsonify(conteudo.listar_categorias(conn))

    @app.post("/api/categorias")
    def nova_cat():
        return jsonify(id=conteudo.criar_categoria(conn, (request.json or {}).get("nome"))), 201

    @app.get("/api/estados")
    def estados(): return jsonify(producao.ESTADOS)

    @app.post("/api/conteudos")
    def novo():
        j = request.json or {}
        return jsonify(id=conteudo.criar_conteudo(conn, j.get("titulo"), j.get("descricao", ""),
                                                   j.get("categoria_id") or None)), 201

    @app.get("/api/conteudos")
    def lista(): return jsonify(conteudo.listar_conteudos(conn, request.args.get("estado")))

    @app.patch("/api/conteudos/<int:cid>/estado")
    def estado(cid):
        producao.mudar_estado(conn, cid, (request.json or {}).get("estado"))
        return jsonify(ok=True)

    @app.post("/api/agenda")
    def agendar():
        j = request.json or {}
        return jsonify(agenda.agendar(conn, j.get("conteudo_id"), j.get("data", ""), j.get("hora", "")))

    @app.get("/api/agenda")
    def ver_agenda(): return jsonify(agenda.listar_agenda(conn))

    @app.get("/api/pendentes")
    def pend(): return jsonify(agenda.pendentes(conn))

    return app
