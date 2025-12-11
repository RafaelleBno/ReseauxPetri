from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    message = "Ceci vient du backend Python"
    return render_template("index.html", msg=message)

@app.route("/calcul")
def calcul():
    resultat = 3 + 5
    return {"resultat": resultat}   # API JSON, utile pour JS

if __name__ == "__main__":
    app.run(debug=True)
