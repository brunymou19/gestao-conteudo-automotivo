"""Cópia de segurança do banco (os registros de materiais, eventos, datas e planejamento).
Execute: python backup.py   (gera backups/conteudo-AAAAMMDD-HHMMSS.db)"""
import os, sqlite3, datetime

if __name__ == "__main__":
    os.makedirs("backups", exist_ok=True)
    destino = f"backups/conteudo-{datetime.datetime.now():%Y%m%d-%H%M%S}.db"
    origem, copia = sqlite3.connect("conteudo.db"), sqlite3.connect(destino)
    origem.backup(copia); copia.close(); origem.close()
    print("Backup criado em", destino)
