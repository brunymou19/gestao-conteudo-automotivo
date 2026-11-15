"""Módulo de Usuário e Acesso (C05): guarda e confere credenciais do administrador."""
from werkzeug.security import generate_password_hash, check_password_hash

TAMANHO_MINIMO_SENHA = 8
_HASH_FALSO = generate_password_hash("senha-falsa")  # igualar o tempo quando o usuário não existe

def criar_usuario(conn, nome, senha):
    nome = (nome or "").strip()
    if not nome:
        raise ValueError("Nome de usuário é obrigatório")
    if len(senha or "") < TAMANHO_MINIMO_SENHA:
        raise ValueError(f"A senha deve ter pelo menos {TAMANHO_MINIMO_SENHA} caracteres")
    try:
        cur = conn.execute("INSERT INTO usuario(nome, senha_hash) VALUES (?,?)",
                           (nome, generate_password_hash(senha)))
    except Exception:
        raise ValueError("Usuário já existe")
    conn.commit()
    return cur.lastrowid

def autenticar(conn, nome, senha):
    """Devolve o id do usuário se nome e senha conferem; senão None."""
    r = conn.execute("SELECT id, senha_hash FROM usuario WHERE nome=?", ((nome or "").strip(),)).fetchone()
    if not r:
        check_password_hash(_HASH_FALSO, senha or "")
        return None
    return r["id"] if check_password_hash(r["senha_hash"], senha or "") else None
