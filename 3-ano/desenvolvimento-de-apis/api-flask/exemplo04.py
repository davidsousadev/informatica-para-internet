from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    return jsonify({"mensagem": "Usuário criado", "dados": dados})

app.run()