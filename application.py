from flask import Flask, render_template, request
from applicationdb import checkUsernameUnique

def returnInvalidInfo(message):
    return render_template("register.html", usernamealert = message)

def checkStringValid(stringToCheck):
    return stringToCheck.isalnum()

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
    nameToCheck = request.form.get("username")
    passToCheck = request.form.get("password")
    passToCheck2 = request.form.get("confirm_password")
    if checkStringValid(nameToCheck) and checkStringValid(passToCheck) and (passToCheck == passToCheck2):
        if checkUsernameUnique(nameToCheck):
            return render_template("registered.html", username=nameToCheck)
        else:
            return returnInvalidInfo("Username already taken")
    else:
        if passToCheck != passToCheck2:
            return returnInvalidInfo("Passwords did not match")
        else:
            return returnInvalidInfo("Please enter an alphanumeric username/password")
