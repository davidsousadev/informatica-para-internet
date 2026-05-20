from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 20},
    {"id": 2, "nome": "Jonas", "idade": 25}
]

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    usuarios[id - 1]["nome"] = dados["nome"]

    return jsonify(usuarios[id - 1])


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuarios.pop(id - 1)

    return jsonify({"mensagem": "Usuário removido"})


app.run()