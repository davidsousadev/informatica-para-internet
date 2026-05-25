# 2. CREATE (Inserir dados)

import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", 
               ("Ana", 25))

conn.commit()
conn.close()