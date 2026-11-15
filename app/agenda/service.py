"""Módulo de Agenda e Publicações (H03, H04, RN03). Usa a interface do módulo de produção."""
from datetime import date, datetime
from app.producao import service as producao

LIMITE_DIARIO = 2          # RN03 (informado pelo cliente)
BLOQUEAR_NO_LIMITE = False # PENDENTE (pergunta nº 1): False = só avisa; True = bloqueia

def _validar(data, hora):
    try:
        datetime.strptime(data, "%Y-%m-%d"); datetime.strptime(hora, "%H:%M")
    except (ValueError, TypeError):
        raise ValueError("Use data AAAA-MM-DD e hora HH:MM")

def agendar(conn, conteudo_id, data, hora):
    _validar(data, hora)
    producao.consultar_estado(conn, conteudo_id)  # garante que existe
    ja_no_dia = conn.execute("SELECT COUNT(*) n FROM agendamento WHERE data=? AND conteudo_id<>?",
                             (data, conteudo_id)).fetchone()["n"]
    excedeu = ja_no_dia >= LIMITE_DIARIO
    if excedeu and BLOQUEAR_NO_LIMITE:
        raise ValueError(f"Limite de {LIMITE_DIARIO} publicações por dia atingido em {data}")
    if conn.execute("SELECT 1 FROM agendamento WHERE data=? AND hora=? AND conteudo_id<>?",
                    (data, hora, conteudo_id)).fetchone():
        raise ValueError("Já existe publicação nesse horário; use horários diferentes")
    conn.execute("INSERT OR REPLACE INTO agendamento(conteudo_id,data,hora) VALUES (?,?,?)",
                 (conteudo_id, data, hora))
    conn.commit()
    producao.mudar_estado(conn, conteudo_id, "agendado")
    return {"alerta": f"Atenção: já há {ja_no_dia} publicações em {data} (limite {LIMITE_DIARIO})."
            if excedeu else None}

def listar_agenda(conn):
    rows = conn.execute("""SELECT a.data, a.hora, c.id, c.titulo, c.estado FROM agendamento a
                           JOIN conteudo c ON c.id=a.conteudo_id ORDER BY a.data, a.hora""")
    hoje = date.today().isoformat()
    return [{**dict(r), "atrasado": r["data"] < hoje and r["estado"] not in producao.ESTADOS_FINAIS}
            for r in rows]

def pendentes(conn):
    """Conteúdos ainda sem data e não finalizados (visão de pendências)."""
    marcas = ",".join("?" * len(producao.ESTADOS_FINAIS))
    rows = conn.execute(f"""SELECT c.id, c.titulo, c.estado FROM conteudo c
        LEFT JOIN agendamento a ON a.conteudo_id=c.id
        WHERE a.conteudo_id IS NULL AND c.estado NOT IN ({marcas}) ORDER BY c.id""",
        producao.ESTADOS_FINAIS)
    return [dict(r) for r in rows]
