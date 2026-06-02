from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Criar banco e tabela
cursor = sqlite3.connect("banco.db")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    ) """)
cursor.close()

# GET - lista usuários
@app.route("/usuarios")
def listar():
    conn = sqlite3.connect("banco.db")
    dados = conn.execute("SELECT * FROM usuarios")
    usuarios = dados.fetchall()
    conn.close()

    return jsonify(usuarios), 200

"""

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.get_json()
    usuario = {
        "id": len(usuarios) + 1,
        "nome": dados.get("nome"),
        "idade": dados.get("idade")
    }
    usuarios.append(usuario)
    return jsonify(["Usuário cadastrado com sucesso!"]), 201

@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    usuarios[id - 1] = {
         "id": id,
        "nome": dados["nome"],
        "idade": dados["idade"]
    }

    return jsonify(usuarios[id - 1])

@app.route("/usuarios/<int:id>", methods=["PATCH"])
def atualizar_usuario_parcial(id):
    dados = request.get_json()

    if "nome" in dados:
        usuarios[id - 1]["nome"] = dados["nome"]

    if "idade" in dados:
        usuarios[id - 1]["idade"] = dados["idade"]

    return jsonify(usuarios[id - 1])

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuarios.pop(id - 1)

    return jsonify({"mensagem": "Usuário removido"})
"""
app.run(debug=True)
