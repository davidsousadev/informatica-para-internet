# 5. DELETE (Excluir dados)
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Ana",))

conn.commit()
conn.close()