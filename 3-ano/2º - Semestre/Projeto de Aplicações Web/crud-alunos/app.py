from flask import Flask, render_template

from controllers.aluno_controller import aluno_controller


app = Flask(__name__)

app.register_blueprint(aluno_controller)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
