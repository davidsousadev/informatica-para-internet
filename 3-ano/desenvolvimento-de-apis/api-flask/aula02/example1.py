from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []
proximo_id = 1

@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    # Use a variável que já existe lá fora.
    global proximo_id

    dados = request.get_json()

    usuario = {
        "id": proximo_id,
        "nome": dados.get("nome"),
        "idade": dados.get("idade")
    }

    usuarios.append(usuario)

    proximo_id += 1

    return jsonify(usuario), 201

app.run()