# -*- coding: utf-8 -*-

from flask import Flask, jsonify, Response
import json

app = Flask(__name__)

# Usando jsonify (Flask)
@app.route("/jsonify")
def exemplo_jsonify():
    return jsonify({
        "mensagem": "Resposta com jsonify",
        "tipo": "flask"
    })


# Usando json (biblioteca padrão)
@app.route("/json")
def exemplo_json():
    dados = {
        "mensagem": "Resposta com json.dumps",
        "tipo": "python"
    }

    return Response(
        json.dumps(dados, ensure_ascii=False),
        content_type="application/json; charset=utf-8"
    )


app.run(debug=True)