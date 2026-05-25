from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana", "idade": 20},
    {"id": 2, "nome": "João", "idade": 25}
]

@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)