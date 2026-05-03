"""

1. Cadastro de Usuários - Crie uma API utilizando Flask que permita cadastrar e listar usuários.

    - A rota POST /usuarios deve receber dados de um usuário e armazená-los em uma lista.
    - A rota GET /usuarios deve retornar todos os usuários cadastrados.


"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os usuários (dados mockados)
usuarios = []

# Rota para cadastrar usuário (POST)
@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.json

    usuario = {
        "nome": dados.get("nome"),
        "idade": dados.get("idade"),
        "cpf": dados.get("cpf")
    }

    usuarios.append(usuario)
    return jsonify("Usuário cadastrado!")

# Rota para listar usuários (GET)
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

# Executar aplicação
app.run()