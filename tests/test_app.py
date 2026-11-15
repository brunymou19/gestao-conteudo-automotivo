import pytest
from app import create_app
from app.agenda import service as agenda

@pytest.fixture
def c(tmp_path):
    return create_app(str(tmp_path / "t.db")).test_client()

def novo(c, t="Opala 78"):
    return c.post("/api/conteudos", json={"titulo": t}).get_json()["id"]

def ag(c, i, hora, data="2026-12-01"):
    return c.post("/api/agenda", json={"conteudo_id": i, "data": data, "hora": hora})

def test_registra_ideia_com_estado_inicial(c):
    novo(c)
    assert c.get("/api/conteudos").get_json()[0]["estado"] == "ideia"

def test_titulo_obrigatorio(c):
    assert c.post("/api/conteudos", json={"titulo": " "}).status_code == 400

def test_estado_invalido_e_valido(c):
    i = novo(c)
    assert c.patch(f"/api/conteudos/{i}/estado", json={"estado": "xyz"}).status_code == 400
    assert c.patch(f"/api/conteudos/{i}/estado", json={"estado": "em_edicao"}).status_code == 200

def test_agendar_muda_estado_e_sai_dos_pendentes(c):
    i = novo(c)
    assert len(c.get("/api/pendentes").get_json()) == 1
    ag(c, i, "10:00")
    assert c.get("/api/pendentes").get_json() == []
    assert c.get("/api/conteudos").get_json()[0]["estado"] == "agendado"

def test_limite_diario_apenas_avisa(c):
    ids = [novo(c, f"c{n}") for n in range(3)]
    r = [ag(c, i, f"1{n}:00").get_json() for n, i in enumerate(ids)]
    assert r[0]["alerta"] is None and r[2]["alerta"] and "limite 2" in r[2]["alerta"]

def test_limite_diario_bloqueia_quando_configurado(c, monkeypatch):
    monkeypatch.setattr(agenda, "BLOQUEAR_NO_LIMITE", True)
    ids = [novo(c, f"c{n}") for n in range(3)]
    assert [ag(c, i, f"1{n}:00").status_code for n, i in enumerate(ids)] == [200, 200, 400]

def test_mesmo_horario_rejeitado(c):
    a, b = novo(c, "a"), novo(c, "b")
    ag(c, a, "10:00")
    assert ag(c, b, "10:00").status_code == 400

def test_atrasado_na_agenda(c):
    i = novo(c)
    ag(c, i, "09:00", "2020-01-01")
    assert c.get("/api/agenda").get_json()[0]["atrasado"] is True

def test_categoria_duplicada(c):
    assert c.post("/api/categorias", json={"nome": "Clássicos"}).status_code == 201
    assert c.post("/api/categorias", json={"nome": "Clássicos"}).status_code == 400
