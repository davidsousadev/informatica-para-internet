from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "David", "idade": 18}
]

@app.route("/")
def index():
    return []

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios), 200

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

app.run(debug=True)









