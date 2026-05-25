# -*- coding: utf-8 -*-

from flask import request, Flask, Response
import json

app = Flask(__name__)

@app.route("/usuarios")
def listar_usuario():
    return []


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json

    resposta = {
        "mensagem": "Usuário criado",
        "dados": dados
    }

    return Response(
        json.dumps(resposta, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )

app.run()