"""Módulo de Gerenciamento de Conteúdo (H01, H07, RN06, RN07)."""
CATEGORIAS_INICIAIS = ["Pelo Caminho", "Na pista", "Garagem da Comunidade", "Agenda automotiva",
    "Entenda sua máquina", "Ícones", "Que carro é esse", "Qual você escolhe", "Top 5", "E se",
    "Bastidores MPM", "Classificados MPM"]
TIPOS_MATERIAL = ("foto", "video", "outro")  # materiais são só REFERÊNCIAS (sem upload)

def semear_categorias(conn):
    if conn.execute("SELECT COUNT(*) FROM categoria").fetchone()[0] == 0:
        conn.executemany("INSERT INTO categoria(nome) VALUES (?)", [(n,) for n in CATEGORIAS_INICIAIS])
        conn.commit()

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
    itens = [dict(r) for r in conn.execute(sql + " ORDER BY c.id DESC", args)]
    for i in itens:
        i["materiais"] = listar_materiais(conn, i["id"])
    return itens

def adicionar_material(conn, conteudo_id, tipo, referencia):
    referencia = (referencia or "").strip()
    if tipo not in TIPOS_MATERIAL:
        raise ValueError(f"Tipo inválido. Use: {', '.join(TIPOS_MATERIAL)}")
    if not referencia:
        raise ValueError("Referência (nome do arquivo, pasta ou link) é obrigatória")
    if not conn.execute("SELECT 1 FROM conteudo WHERE id=?", (conteudo_id,)).fetchone():
        raise LookupError("Conteúdo não encontrado")
    cur = conn.execute("INSERT INTO material(conteudo_id,tipo,referencia) VALUES (?,?,?)",
                       (conteudo_id, tipo, referencia))
    conn.commit()
    return cur.lastrowid

def listar_materiais(conn, conteudo_id):
    return [dict(r) for r in conn.execute("SELECT id,tipo,referencia FROM material WHERE conteudo_id=? ORDER BY id",
                                          (conteudo_id,))]

def remover_material(conn, material_id):
    if conn.execute("DELETE FROM material WHERE id=?", (material_id,)).rowcount == 0:
        raise LookupError("Material não encontrado")
    conn.commit()
