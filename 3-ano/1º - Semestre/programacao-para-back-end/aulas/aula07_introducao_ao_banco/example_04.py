# 4. UPDATE (Atualizar dados)
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

id = int(input("Escolha o usuario por id: "))
novo_nome = str(input("Digite seu novo nome: "))
nova_idade = int(input("Digite sua idade: "))
cursor.execute("UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?", (novo_nome,nova_idade, id))

conn.commit()
conn.close()