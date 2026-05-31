# 3. READ (Consultar dados)

import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conn.close()