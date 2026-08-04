from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "banco.db"

# Cria a tabela
conn = sqlite3.connect(DB)
conn.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")
conn.close()

# Lista todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar():
    conn = sqlite3.connect(DB)
    usuarios = conn.execute(
        "SELECT * FROM usuarios"
    ).fetchall()
    conn.close()

    return jsonify(usuarios)

# Busca usuário pelo ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar(id):
    conn = sqlite3.connect(DB)
    usuario = conn.execute(
        "SELECT id, nome FROM usuarios WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify({
        "id": usuario[0],
        "nome": usuario[1]
    })

# Cria usuário
@app.route("/usuarios", methods=["POST"])
def criar():
    dados = request.get_json()

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Informe o nome"}), 400

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome) VALUES (?)",
        (dados["nome"],)
    )

    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "id": novo_id,
        "nome": dados["nome"]
    }), 201

# Atualiza usuário
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Informe o nome"}), 400

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE usuarios SET nome = ? WHERE id = ?",
        (dados["nome"], id)
    )

    conn.commit()
    alterados = cursor.rowcount
    conn.close()

    if alterados == 0:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify({
        "id": id,
        "nome": dados["nome"]
    })

# Remove usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id,)
    )

    conn.commit()
    removidos = cursor.rowcount
    conn.close()

    if removidos == 0:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify({
        "mensagem": "Usuário removido"
    })

app.run(debug=True)