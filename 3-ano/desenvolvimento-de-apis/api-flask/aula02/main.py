from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/")
def index():
    return []

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.get_json()

    usuario = {
        "id": len(usuarios) + 1,
        "nome": dados.get("nome"),
        "idade": dados.get("idade")
    }

    usuarios.append(usuario)

    return jsonify(usuario), 201


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios), 200


app.run()