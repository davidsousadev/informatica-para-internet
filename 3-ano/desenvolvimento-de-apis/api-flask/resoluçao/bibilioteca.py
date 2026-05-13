"""

2. Cadastro de Livros - Crie uma API para gerenciar livros de uma biblioteca.
-​ A rota POST /livros deve permitir o cadastro de um novo livro.
-​ A rota GET /livros deve retornar a lista de todos os livros cadastrados.

"""


from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {
        "nome": "O Pequeno Príncipe",
        "paginas": 71
    },
    {
        "nome": "Mar Morto",
        "paginas": 458
    }
]

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

app.run(debug=True)