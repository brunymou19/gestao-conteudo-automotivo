import pytest
from app import create_app
from app.acesso import service as acesso

@pytest.fixture
def app(tmp_path):
    a = create_app(str(tmp_path / "t.db"), secret_key="teste")
    acesso.criar_usuario(a.config["CONN"], "admin", "senha12345")
    return a

def entrar(cli, senha="senha12345"):
    return cli.post("/login", data={"usuario": "admin", "senha": senha})

def test_api_sem_login_retorna_401(app):
    assert app.test_client().get("/api/conteudos").status_code == 401

def test_pagina_sem_login_redireciona(app):
    r = app.test_client().get("/")
    assert r.status_code == 302 and "/login" in r.headers["Location"]

def test_senha_errada_negada(app):
    cli = app.test_client()
    assert entrar(cli, "errada").status_code == 401
    assert cli.get("/api/conteudos").status_code == 401

def test_usuario_inexistente_negado(app):
    r = app.test_client().post("/login", data={"usuario": "x", "senha": "senha12345"})
    assert r.status_code == 401

def test_senha_certa_libera(app):
    cli = app.test_client()
    assert entrar(cli).status_code == 302
    assert cli.get("/api/conteudos").status_code == 200

def test_logout_bloqueia_de_novo(app):
    cli = app.test_client(); entrar(cli)
    cli.post("/logout")
    assert cli.get("/api/conteudos").status_code == 401

def test_senha_guardada_como_hash(app):
    h = app.config["CONN"].execute("SELECT senha_hash FROM usuario").fetchone()[0]
    assert h != "senha12345" and "senha12345" not in h

def test_senha_curta_e_usuario_duplicado(app):
    conn = app.config["CONN"]
    with pytest.raises(ValueError): acesso.criar_usuario(conn, "novo", "curta")
    with pytest.raises(ValueError): acesso.criar_usuario(conn, "admin", "outrasenha123")
