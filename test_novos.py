from datetime import date
import pytest
from app import create_app
from app.acesso import service as acesso
from app.agenda import service as agenda
from app.conteudo import service as cs

@pytest.fixture
def ctx(tmp_path):
    app = create_app(str(tmp_path / "t.db"), secret_key="t")
    acesso.criar_usuario(app.config["CONN"], "admin", "senha12345")
    cli = app.test_client()
    cli.post("/login", data={"usuario": "admin", "senha": "senha12345"})
    return cli, app.config["CONN"]

def novo(c, t="Opala"):
    return c.post("/api/conteudos", json={"titulo": t}).get_json()["id"]

def ag(c, i, hora, data="2026-12-01"):
    return c.post("/api/agenda", json={"conteudo_id": i, "data": data, "hora": hora})

def test_12_categorias_iniciais(ctx):
    nomes = [x["nome"] for x in ctx[0].get("/api/categorias").get_json()]
    assert len(nomes) == 12 and "Top 5" in nomes and "Classificados MPM" in nomes

def test_material_por_referencia(ctx):
    c, _ = ctx; i = novo(c)
    r = c.post(f"/api/conteudos/{i}/materiais", json={"tipo": "foto", "referencia": "IMG_1.jpg"})
    assert r.status_code == 201
    assert c.get("/api/conteudos").get_json()[0]["materiais"][0]["referencia"] == "IMG_1.jpg"
    assert c.post(f"/api/conteudos/{i}/materiais", json={"tipo": "zip", "referencia": "x"}).status_code == 400
    assert c.delete(f"/api/materiais/{r.get_json()['id']}").status_code == 200

def test_mover_mantem_hora_e_exige_agendamento(ctx):
    c, _ = ctx; i = novo(c)
    assert c.patch(f"/api/agenda/{i}", json={"data": "2026-12-05"}).status_code == 404
    ag(c, i, "10:00")
    assert c.patch(f"/api/agenda/{i}", json={"data": "2026-12-05"}).status_code == 200
    a = c.get("/api/agenda").get_json()[0]
    assert (a["data"], a["hora"]) == ("2026-12-05", "10:00")

def test_mover_para_horario_ocupado_falha(ctx):
    c, _ = ctx; a, b = novo(c, "a"), novo(c, "b")
    ag(c, a, "10:00", "2026-12-01"); ag(c, b, "10:00", "2026-12-02")
    assert c.patch(f"/api/agenda/{b}", json={"data": "2026-12-01"}).status_code == 400

def test_conteudo_finalizado_nao_agenda(ctx):
    c, _ = ctx; i = novo(c)
    c.patch(f"/api/conteudos/{i}/estado", json={"estado": "publicado"})
    assert ag(c, i, "10:00").status_code == 400

def test_evento_fluxo_completo(ctx):
    c, _ = ctx
    base = {"nome": "Encontro MPM", "data": "2026-12-10", "solicitante": "Organização", "tipo": "divulgacao_antecipada", "prazo": "2026-12-05"}
    assert c.post("/api/eventos", json={**base, "tipo": "x"}).status_code == 400
    eid = c.post("/api/eventos", json=base).get_json()["id"]
    assert c.post(f"/api/eventos/{eid}/agendar", json={"data": "2026-12-04", "hora": "09:00"}).status_code == 200
    cont = c.get("/api/conteudos").get_json()[0]
    assert cont["titulo"] == "Evento: Encontro MPM" and cont["estado"] == "agendado" and cont["categoria"] == "Agenda automotiva"
    assert c.patch(f"/api/eventos/{eid}/situacao", json={"situacao": "concluido"}).status_code == 200

def test_evento_passado_aceito_e_atrasado(ctx):
    c, _ = ctx
    c.post("/api/eventos", json={"nome": "Antigo", "data": "2020-01-01", "solicitante": "Fulano", "tipo": "publicacao_posterior"})
    assert c.get("/api/eventos").get_json()[0]["atrasado"] is True

def test_oportunidade(ctx):
    c, _ = ctx
    assert c.post("/api/oportunidades", json={"contato": "Loja X", "canal": "fax", "proposta": "p"}).status_code == 400
    oid = c.post("/api/oportunidades", json={"contato": "Loja X", "canal": "instagram", "proposta": "Divulgar peças", "condicoes": "2 posts"}).get_json()["id"]
    assert c.patch(f"/api/oportunidades/{oid}/situacao", json={"situacao": "aceita"}).status_code == 200
    assert c.patch(f"/api/oportunidades/{oid}/situacao", json={"situacao": "?"}).status_code == 400

def test_regra_semanal_gera_sugestao_ate_agendar(ctx):
    _, conn = ctx
    domingo = date(2026, 11, 15)
    agenda.definir_regra(conn, 6, "encontro da semana")
    assert [s["data"] for s in agenda.sugestoes(conn, 8, domingo)] == ["2026-11-15", "2026-11-22"]
    cid = cs.criar_conteudo(conn, "Encontro")
    agenda.agendar(conn, cid, "2026-11-15", "10:00")
    assert [s["data"] for s in agenda.sugestoes(conn, 8, domingo)] == ["2026-11-22"]

def test_regra_invalida(ctx):
    with pytest.raises(ValueError): agenda.definir_regra(ctx[1], 9, "x")
