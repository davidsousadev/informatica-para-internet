from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Criar banco e tabela
conn = sqlite3.connect("banco.db")
conn.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
conn.close()

app.run()