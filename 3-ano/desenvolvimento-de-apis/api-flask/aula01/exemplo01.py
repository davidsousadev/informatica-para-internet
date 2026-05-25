from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/canetas")
def canetas():
    return "<p>Hello, canetas!</p>"

@app.route("/usuarios")
def usuarios():
    return "<p>Hello, usuarios!</p>"

app.run()