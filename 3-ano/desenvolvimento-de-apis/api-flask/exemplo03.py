from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuarios/<nome>")
def usuario(nome):
    return jsonify({"usuario": nome})

@app.route("/usuarios")
def usuarios():
    return jsonify({ })

app.run()
