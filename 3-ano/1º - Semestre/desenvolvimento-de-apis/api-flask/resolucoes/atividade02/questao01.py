from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/usuarios", methods=["POST"])

def adicionar_usuario():
    
    dados = request.json
    
    usuario = {
    
       "nome": dados.get("nome"),
       "idade": dados.get("idade")
    
    }
    
    usuarios.append(usuario)
    
    return jsonify(usuario)
    
    
@app.route("/usuarios", methods=["GET"])

def listar_usuarios():
    
    return jsonify(usuarios)
    
app.run()