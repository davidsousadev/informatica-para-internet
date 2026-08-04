# 5. DELETE (Excluir dados)
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()
id = int(input("Digite o id para excluir: "))
cursor.execute(f"DELETE FROM usuarios WHERE id = {id}")
# cursor.execute("DELETE FROM usuarios WHERE id = ?",(id))
conn.commit()
conn.close()