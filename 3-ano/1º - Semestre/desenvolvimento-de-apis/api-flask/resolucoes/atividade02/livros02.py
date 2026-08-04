from flask import Flask, request, jsonify

app = Flask(__name__)

livros = []

@app.route("/livros", methods=["POST"])
def colocar_livros():
    dados = request.json
    livro = {
       "Titulo": dados.get("titulo"),
       "Autor": dados.get("autor")
    }
    livros.append(livro)
    return jsonify(livro)
    
    
@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)
    
app.run()