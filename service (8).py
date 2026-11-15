"""Módulo de Produção: dono do fluxo de estados (RN01)."""
# Estados confirmados pelo cliente (ideia, em edição, pronto, agendado, publicado, encerrado).
ESTADOS = ["ideia", "em_edicao", "pronto", "agendado", "publicado", "encerrado"]
ESTADOS_FINAIS = ("publicado", "encerrado")

def mudar_estado(conn, conteudo_id, estado):
    if estado not in ESTADOS:
        raise ValueError(f"Estado inválido. Use um de: {', '.join(ESTADOS)}")
    cur = conn.execute("UPDATE conteudo SET estado=? WHERE id=?", (estado, conteudo_id))
    if cur.rowcount == 0:
        raise LookupError("Conteúdo não encontrado")
    conn.commit()

def consultar_estado(conn, conteudo_id):
    r = conn.execute("SELECT estado FROM conteudo WHERE id=?", (conteudo_id,)).fetchone()
    if not r:
        raise LookupError("Conteúdo não encontrado")
    return r["estado"]
