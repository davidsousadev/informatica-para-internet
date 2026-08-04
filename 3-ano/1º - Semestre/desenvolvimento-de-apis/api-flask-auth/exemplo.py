from flask import *

app = Flask(__name__)
app.secret_key = "300-info"

USUARIO = "angelo"
SENHA = "angelo"

@app.route("/")
def home():
    if "usuario" in session:
        return f"""
        <p>300-Info The Best!</p>
        
        <a href="/logout">Sair</a>
        """
    return redirect(url_for("login"))


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == USUARIO and senha == SENHA:
            session["usuario"] = usuario
            return redirect(url_for("home"))
          
    return render_template_string("""
    <form method="post">
            <input type="text" name="usuario" placeholder="Usuário"><br>
            <input type="text" name="senha" placeholder="Senha"><br>
            <button type="submit">Entrar</button>
        </form>
""")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


app.run()
