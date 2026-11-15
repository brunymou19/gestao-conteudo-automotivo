import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS conteudo (
    id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descricao TEXT DEFAULT '',
    categoria_id INTEGER REFERENCES categoria(id), estado TEXT NOT NULL DEFAULT 'ideia',
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS agendamento (
    conteudo_id INTEGER PRIMARY KEY REFERENCES conteudo(id),
    data TEXT NOT NULL, hora TEXT NOT NULL, UNIQUE(data, hora));
"""

def conectar(caminho):
    conn = sqlite3.connect(caminho, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    conn.executescript(SCHEMA_ACESSO)
    return conn

SCHEMA_ACESSO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE, senha_hash TEXT NOT NULL);
"""
