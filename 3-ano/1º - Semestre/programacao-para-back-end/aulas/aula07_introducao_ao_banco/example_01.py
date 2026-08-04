# 1. Criando conexão e tabela

import sqlite3

# cria/conecta ao banco (arquivo .db)
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")

conn.commit()
conn.close()