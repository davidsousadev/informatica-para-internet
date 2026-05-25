# 4. UPDATE (Atualizar dados)
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", 
               (30, "Ana"))

conn.commit()
conn.close()