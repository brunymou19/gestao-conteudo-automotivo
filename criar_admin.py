"""Cria o administrador do sistema. Execute uma vez: python criar_admin.py"""
import getpass
from app.db import conectar
from app.acesso import service as acesso

if __name__ == "__main__":
    conn = conectar("conteudo.db")
    nome = input("Usuário: ")
    senha = getpass.getpass("Senha (mínimo 8 caracteres): ")
    if senha != getpass.getpass("Repita a senha: "):
        raise SystemExit("As senhas não conferem.")
    try:
        acesso.criar_usuario(conn, nome, senha)
        print("Administrador criado com sucesso.")
    except ValueError as e:
        raise SystemExit(f"Erro: {e}")
