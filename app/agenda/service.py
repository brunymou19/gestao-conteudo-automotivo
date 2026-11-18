"""Módulo de Agenda e Publicações (H03, H04, RN03). Usa a interface do módulo de produção."""
from datetime import date, datetime, timedelta
from app.producao import service as producao

LIMITE_DIARIO = 2           # RN03 (informado pelo cliente)
BLOQUEAR_NO_LIMITE = False  # cliente definiu: o sistema apenas AVISA
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

def _validar(data, hora):
    try:
        datetime.strptime(data, "%Y-%m-%d"); datetime.strptime(hora, "%H:%M")
    except (ValueError, TypeError):
        raise ValueError("Use data AAAA-MM-DD e hora HH:MM")

def agendar(conn, conteudo_id, data, hora):
    _validar(data, hora)
    if producao.consultar_estado(conn, conteudo_id) in producao.ESTADOS_FINAIS:
        raise ValueError("Conteúdo já finalizado não pode ser agendado")
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

def mover(conn, conteudo_id, data, hora=None):
    """Reorganiza a agenda: muda a data (e opcionalmente a hora) de um conteúdo já agendado."""
    r = conn.execute("SELECT hora FROM agendamento WHERE conteudo_id=?", (conteudo_id,)).fetchone()
    if not r:
        raise LookupError("Conteúdo não está na agenda")
    return agendar(conn, conteudo_id, data, hora or r["hora"])

def listar_agenda(conn):
    rows = conn.execute("""SELECT a.data, a.hora, c.id, c.titulo, c.estado FROM agendamento a
                           JOIN conteudo c ON c.id=a.conteudo_id ORDER BY a.data, a.hora""")
    hoje = date.today().isoformat()
    return [{**dict(r), "atrasado": r["data"] < hoje and r["estado"] not in producao.ESTADOS_FINAIS}
            for r in rows]

def pendentes(conn):
    """Conteúdos ainda sem data e não finalizados."""
    marcas = ",".join("?" * len(producao.ESTADOS_FINAIS))
    rows = conn.execute(f"""SELECT c.id, c.titulo, c.estado FROM conteudo c
        LEFT JOIN agendamento a ON a.conteudo_id=c.id
        WHERE a.conteudo_id IS NULL AND c.estado NOT IN ({marcas}) ORDER BY c.id""",
        producao.ESTADOS_FINAIS)
    return [dict(r) for r in rows]

# --- Regras semanais: conteúdos fixos em dias da semana viram sugestões na agenda ---
def definir_regra(conn, dia_semana, descricao, categoria_id=None):
    if dia_semana not in range(7):
        raise ValueError("dia_semana deve ser de 0 (segunda) a 6 (domingo)")
    if not (descricao or "").strip():
        raise ValueError("Descrição é obrigatória")
    conn.execute("INSERT OR REPLACE INTO regra_semanal VALUES (?,?,?)",
                 (dia_semana, descricao.strip(), categoria_id or None))
    conn.commit()

def listar_regras(conn):
    return [{**dict(r), "dia": DIAS[r["dia_semana"]]}
            for r in conn.execute("SELECT * FROM regra_semanal ORDER BY dia_semana")]

def remover_regra(conn, dia_semana):
    if conn.execute("DELETE FROM regra_semanal WHERE dia_semana=?", (dia_semana,)).rowcount == 0:
        raise LookupError("Regra não encontrada")
    conn.commit()

def sugestoes(conn, dias=14, hoje=None):
    """Dias dos próximos `dias` que têm regra semanal e ainda não têm o conteúdo fixo agendado."""
    hoje = hoje or date.today()
    regras = {r["dia_semana"]: r for r in conn.execute("SELECT * FROM regra_semanal")}
    saida = []
    for i in range(dias):
        d = hoje + timedelta(days=i)
        r = regras.get(d.weekday())
        if not r:
            continue
        sql = "SELECT 1 FROM agendamento a JOIN conteudo c ON c.id=a.conteudo_id WHERE a.data=?"
        args = [d.isoformat()]
        if r["categoria_id"]:
            sql += " AND c.categoria_id=?"; args.append(r["categoria_id"])
        if not conn.execute(sql, args).fetchone():
            saida.append({"data": d.isoformat(), "dia": DIAS[d.weekday()],
                          "descricao": r["descricao"], "categoria_id": r["categoria_id"]})
    return saida
