from flask import Flask, render_template, request, redirect
from applicationdb import checkUsernameUnique, updateAccountDB

def returnInvalidInfo(message):
    return render_template("register.html", usernamealert = message)

def checkStringValid(stringToCheck):
    return stringToCheck.isalnum()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contactme.html")

@app.route("/success")
def successful():
    return render_template("registered.html", username=request.form.get("username"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registerattempt", methods=["POST"])
def tryRegister():
    nameToCheck = request.form.get("username")
    passToCheck = request.form.get("password")
    passToCheck2 = request.form.get("confirm_password")
    if checkStringValid(nameToCheck) and checkStringValid(passToCheck) and (passToCheck == passToCheck2):
        if checkUsernameUnique(nameToCheck):
            updateAccountDB(nameToCheck, passToCheck)
            return redirect("/success")
        else:
            return returnInvalidInfo("Username already taken")
    else:
        if passToCheck != passToCheck2:
            return returnInvalidInfo("Passwords did not match")
        else:
            return returnInvalidInfo("Please enter an alphanumeric username/password")

@app.route("/register")
def register():
    return render_template("register.html")
