from flask import request, Flask, jsonify

app = Flask(__name__)


usuarios = []

@app.route("/usuarios", methods=["POST"])
def adicionar():
    dados = request.json
    usuarios.append(dados)
    return jsonify(usuarios)

@app.route("/usuarios", methods=["GET"])
def listar():
    return jsonify(usuarios)

app.run()