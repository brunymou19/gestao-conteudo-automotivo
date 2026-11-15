"""Módulo de Gerenciamento de Conteúdo (H01, H07, RN06)."""

def criar_categoria(conn, nome):
    nome = (nome or "").strip()
    if not nome:
        raise ValueError("Nome da categoria é obrigatório")
    try:
        cur = conn.execute("INSERT INTO categoria(nome) VALUES (?)", (nome,))
    except Exception:
        raise ValueError("Categoria já existe")
    conn.commit()
    return cur.lastrowid

def listar_categorias(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM categoria ORDER BY nome")]

def criar_conteudo(conn, titulo, descricao="", categoria_id=None):
    titulo = (titulo or "").strip()
    if not titulo:
        raise ValueError("Título é obrigatório")
    cur = conn.execute("INSERT INTO conteudo(titulo, descricao, categoria_id) VALUES (?,?,?)",
                       (titulo, descricao, categoria_id))
    conn.commit()
    return cur.lastrowid

def listar_conteudos(conn, estado=None):
    sql = """SELECT c.*, k.nome AS categoria, a.data, a.hora FROM conteudo c
             LEFT JOIN categoria k ON k.id=c.categoria_id
             LEFT JOIN agendamento a ON a.conteudo_id=c.id"""
    args = ()
    if estado:
        sql += " WHERE c.estado=?"; args = (estado,)
    return [dict(r) for r in conn.execute(sql + " ORDER BY c.id DESC", args)]
