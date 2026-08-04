# pip install flask flask-sqlalchemy flask-jwt-extended werkzeug

from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
import sqlite3

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "segredo"

jwt = JWTManager(app)


# ==================================
# BANCO
# ==================================

def conectar():

    conn = sqlite3.connect(
        "usuarios.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    conn.commit()

    return conn, cursor


# ==================================
# HOME
# ==================================

@app.route("/")
def index():

    return jsonify({
        "mensagem":
        "API funcionando"
    })


# ==================================
# LOGIN
# ==================================

@app.route("/login", methods=["POST"])
def login():

    dados = request.get_json()

    conn, cursor = conectar()

    cursor.execute(
        """
        SELECT *
        FROM usuarios
        WHERE email = ?
        """,
        (dados["email"],)
    )

    usuario = cursor.fetchone()

    conn.close()

    if not usuario:
        return jsonify({
            "erro":
            "Usuário não encontrado"
        }), 404

    if not check_password_hash(
        usuario["senha"],
        dados["senha"]
    ):
        return jsonify({
            "erro":
            "Senha inválida"
        }), 401

    token = create_access_token(
        identity=str(usuario["id"])
    )

    return jsonify({
        "token": token
    })


# ==================================
# CREATE
# ==================================

@app.route("/usuarios", methods=["POST"])
def criar_usuario():

    dados = request.get_json()

    conn, cursor = conectar()

    try:

        cursor.execute(
            """
            INSERT INTO usuarios
            (
                nome,
                idade,
                email,
                senha
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                dados["nome"],
                dados["idade"],
                dados["email"],
                generate_password_hash(
                    dados["senha"]
                )
            )
        )

        conn.commit()

        return jsonify({
            "mensagem":
            "Usuário criado"
        }), 201

    except sqlite3.IntegrityError:

        return jsonify({
            "erro":
            "Email já cadastrado"
        }), 400

    finally:
        conn.close()


# ==================================
# READ ALL
# ==================================

@app.route("/usuarios", methods=["GET"])
@jwt_required()
def listar_usuarios():

    conn, cursor = conectar()

    cursor.execute(
        "SELECT id, nome, idade, email FROM usuarios"
    )

    usuarios = [
        dict(usuario)
        for usuario in cursor.fetchall()
    ]

    conn.close()

    return jsonify(usuarios)


# ==================================
# READ ONE
# ==================================

@app.route("/usuarios/<int:id>")
@jwt_required()
def buscar_usuario(id):

    conn, cursor = conectar()

    cursor.execute(
        """
        SELECT
            id,
            nome,
            idade,
            email
        FROM usuarios
        WHERE id = ?
        """,
        (id,)
    )

    usuario = cursor.fetchone()

    conn.close()

    if not usuario:
        return jsonify({
            "erro":
            "Usuário não encontrado"
        }), 404

    return jsonify(dict(usuario))


# ==================================
# UPDATE
# ==================================

@app.route(
    "/usuarios/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def atualizar_usuario(id):

    dados = request.get_json()

    conn, cursor = conectar()

    cursor.execute(
        """
        UPDATE usuarios
        SET
            nome = ?,
            idade = ?,
            email = ?
        WHERE id = ?
        """,
        (
            dados["nome"],
            dados["idade"],
            dados["email"],
            id
        )
    )

    conn.commit()

    conn.close()

    return jsonify({
        "mensagem":
        "Usuário atualizado"
    })


# ==================================
# DELETE
# ==================================

@app.route(
    "/usuarios/<int:id>",
    methods=["DELETE"]
)
@jwt_required()
def deletar_usuario(id):

    conn, cursor = conectar()

    cursor.execute(
        """
        DELETE FROM usuarios
        WHERE id = ?
        """,
        (id,)
    )

    conn.commit()

    conn.close()

    return jsonify({
        "mensagem":
        "Usuário removido"
    })


if __name__ == "__main__":
    app.run(debug=True)