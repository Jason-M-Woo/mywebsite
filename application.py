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
    if request.form.get("username") == "" :
        return render_template("register.html", usernamealert = "Please enter a valid username")
    else:
        username = request.form.get("username")
        return render_template("registered.html", username=username)


    #password = request.form.get("password")
