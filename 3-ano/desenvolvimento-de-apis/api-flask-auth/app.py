from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "segredo"

USUARIO = "admin"
SENHA = "123456"

@app.route("/")
def home():
    if "usuario" in session:
        return f"""
        <h1>Olá, {session['usuario']}!</h1>
        <a href="/logout">Sair</a>
        """
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == USUARIO and senha == SENHA:
            session["usuario"] = usuario
            return redirect(url_for("home"))

        return "Usuário ou senha inválidos", 401

    return render_template_string("""
        <form method="post">
            <input type="text" name="usuario" placeholder="Usuário"><br>
            <input type="password" name="senha" placeholder="Senha"><br>
            <button type="submit">Entrar</button>
        </form>
    """)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)