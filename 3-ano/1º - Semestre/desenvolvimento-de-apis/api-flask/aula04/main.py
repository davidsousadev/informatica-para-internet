from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 20},
    {"id": 2, "nome": "Jonas", "idade": 25}
]

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios), 200

# Atualização Total
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()

    usuarios[id - 1] = {
        "id": id,
        "nome": dados["nome"],
        "idade": dados["idade"]
    }

    return jsonify(usuarios[id - 1])

# Atualização Parcial
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

app.run(debug=True)