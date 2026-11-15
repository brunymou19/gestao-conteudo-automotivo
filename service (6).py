"""Módulo de Eventos e Oportunidades (H05, H06, RN02, RN04, RN08)."""
from datetime import date, datetime
from app.conteudo import service as conteudo
from app.agenda import service as agenda

TIPOS_EVENTO = ["divulgacao_antecipada", "cobertura_durante", "publicacao_posterior"]  # RN02
SITUACOES_EVENTO = ["pendente", "concluido", "cancelado"]
CANAIS = ["instagram", "email", "outro"]
# PROVISÓRIO: o cliente não definiu os valores de situação das oportunidades
SITUACOES_OPORTUNIDADE = ["nova", "em_conversa", "aceita", "recusada", "concluida"]

def _data(v, nome):
    try:
        datetime.strptime(v, "%Y-%m-%d")
    except (ValueError, TypeError):
        raise ValueError(f"{nome} deve estar no formato AAAA-MM-DD")

def criar_evento(conn, nome, data, solicitante, tipo, prazo=None):
    nome, solicitante = (nome or "").strip(), (solicitante or "").strip()
    if not nome or not solicitante:
        raise ValueError("Nome do evento e quem pediu são obrigatórios")
    if tipo not in TIPOS_EVENTO:
        raise ValueError(f"Tipo inválido. Use: {', '.join(TIPOS_EVENTO)}")
    _data(data, "Data")  # datas passadas são aceitas: o cliente pode lançar depois
    if prazo:
        _data(prazo, "Prazo")
    cur = conn.execute("INSERT INTO evento(nome,data,solicitante,tipo,prazo) VALUES (?,?,?,?,?)",
                       (nome, data, solicitante, tipo, prazo or None))
    conn.commit()
    return cur.lastrowid

def listar_eventos(conn):
    hoje = date.today().isoformat()
    rows = conn.execute("SELECT * FROM evento ORDER BY COALESCE(prazo,data), id")
    return [{**dict(r), "atrasado": r["situacao"] == "pendente" and (r["prazo"] or r["data"]) < hoje}
            for r in rows]

def _mudar(conn, tabela, id_, situacao, validas):
    if situacao not in validas:
        raise ValueError(f"Situação inválida. Use: {', '.join(validas)}")
    if conn.execute(f"UPDATE {tabela} SET situacao=? WHERE id=?", (situacao, id_)).rowcount == 0:
        raise LookupError("Registro não encontrado")
    conn.commit()

def mudar_situacao_evento(conn, evento_id, situacao):
    _mudar(conn, "evento", evento_id, situacao, SITUACOES_EVENTO)

def gerar_conteudo(conn, evento_id):
    ev = conn.execute("SELECT * FROM evento WHERE id=?", (evento_id,)).fetchone()
    if not ev:
        raise LookupError("Evento não encontrado")
    if ev["conteudo_id"]:
        return ev["conteudo_id"]
    cat = conn.execute("SELECT id FROM categoria WHERE nome='Agenda automotiva'").fetchone()
    cid = conteudo.criar_conteudo(conn, f"Evento: {ev['nome']}",
                                  f"Pedido de {ev['solicitante']} ({ev['tipo']})", cat["id"] if cat else None)
    conn.execute("UPDATE evento SET conteudo_id=? WHERE id=?", (cid, evento_id))
    conn.commit()
    return cid

def agendar_evento(conn, evento_id, data, hora):
    """Gera (se preciso) o conteúdo do evento e o coloca na agenda."""
    return agenda.agendar(conn, gerar_conteudo(conn, evento_id), data, hora)

def criar_oportunidade(conn, contato, canal, proposta, condicoes=""):
    contato, proposta = (contato or "").strip(), (proposta or "").strip()
    if not contato or not proposta:
        raise ValueError("Nome do contato e proposta são obrigatórios")
    if canal not in CANAIS:
        raise ValueError(f"Canal inválido. Use: {', '.join(CANAIS)}")
    cur = conn.execute("INSERT INTO oportunidade(contato,canal,proposta,condicoes) VALUES (?,?,?,?)",
                       (contato, canal, proposta, condicoes or ""))
    conn.commit()
    return cur.lastrowid

def listar_oportunidades(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM oportunidade ORDER BY id DESC")]

def mudar_situacao_oportunidade(conn, oportunidade_id, situacao):
    _mudar(conn, "oportunidade", oportunidade_id, situacao, SITUACOES_OPORTUNIDADE)
