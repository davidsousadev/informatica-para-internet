from flask import Flask, request, jsonify

app = Flask(__name__)

filmes = [
    {
        "id": 1,
        "titulo": "O agente secreto",
        "genero": "Ação",
        "ano": 2025
        }

]

@app.route("/filmes", methods=["POST"])
def cadastrar_filmes():
    pass

@app.route("/filmes/<int:id>")
def listar_um_filme(id):
    filme = filmes[id - 1]
    return jsonify(filme), 200

app.run(debug=True)