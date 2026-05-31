# 4. UPDATE (Atualizar dados)
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

id = int(input("Escolha o usuario por id: "))
novo_nome = str(input("Digite seu novo nome: "))
cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, id))

conn.commit()
conn.close()