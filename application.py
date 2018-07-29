from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contactme.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/success", methods=["POST"])
def registered():
    username = request.form.get("username")
    #password = request.form.get("password")
    return render_template("registered.html", username=username)
