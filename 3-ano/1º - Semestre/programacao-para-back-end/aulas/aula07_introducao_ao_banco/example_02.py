# 2. CREATE (Inserir dados)

import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))

conn.commit()
conn.close()