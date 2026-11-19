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
    conn.executescript(SCHEMA_EXTRA)
    return conn

SCHEMA_ACESSO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE, senha_hash TEXT NOT NULL);
"""

SCHEMA_EXTRA = """
CREATE TABLE IF NOT EXISTS material (
    id INTEGER PRIMARY KEY AUTOINCREMENT, conteudo_id INTEGER NOT NULL REFERENCES conteudo(id),
    tipo TEXT NOT NULL, referencia TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS evento (
    id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, data TEXT NOT NULL,
    solicitante TEXT NOT NULL, tipo TEXT NOT NULL, prazo TEXT,
    situacao TEXT NOT NULL DEFAULT 'pendente', conteudo_id INTEGER REFERENCES conteudo(id));
CREATE TABLE IF NOT EXISTS oportunidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT, contato TEXT NOT NULL, canal TEXT NOT NULL,
    proposta TEXT NOT NULL, condicoes TEXT DEFAULT '', situacao TEXT NOT NULL DEFAULT 'nova',
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS regra_semanal (
    dia_semana INTEGER PRIMARY KEY, descricao TEXT NOT NULL, categoria_id INTEGER REFERENCES categoria(id));
"""
