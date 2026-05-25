from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Criar banco e tabela
conn = sqlite3.connect("banco.db")
conn.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
conn.close()

# GET - lista usuários
@app.route("/usuarios")
def listar():
    conn = sqlite3.connect("banco.db")
    usuarios = conn.execute("SELECT * FROM usuarios").fetchall()
    conn.close()

    return jsonify(usuarios)

# POST - Cria usuário
@app.route("/usuarios", methods=["POST"])
def criar():
    dados = request.get_json()

    conn = sqlite3.connect("banco.db")
    conn.execute("INSERT INTO usuarios (nome) VALUES (?)", (dados["nome"],))
    conn.commit()
    conn.close()

    return jsonify("Usuario cadastrado com sucesso!"), 201

app.run()