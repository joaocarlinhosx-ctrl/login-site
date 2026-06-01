from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/entrar", methods=["POST"])
def entrar():
    email = request.form["email"]
    senha = request.form["senha"]

    print("Usuário:", email)
    print("Senha:", senha)

    return render_template("sucesso.html")

if __name__ == "__main__":
    app.run(debug=True)