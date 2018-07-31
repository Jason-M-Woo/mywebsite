from flask import Flask, render_template, request, redirect
from applicationdb import checkUsernameUnique, updateAccountDB, checkLoginInfo

def returnInvalidInfo(webpage, message):
    return render_template(webpage, usernamealert = message)

def checkStringValid(stringToCheck):
    return stringToCheck.isalnum()

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contactme.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        nameToCheck = request.form.get("username")
        passToCheck = request.form.get("password")
        passToCheck2 = request.form.get("confirm_password")
        if checkStringValid(nameToCheck) and checkStringValid(passToCheck) and (passToCheck == passToCheck2) and (len(nameToCheck) < 17) and (len(passToCheck) > 7):
            if checkUsernameUnique(nameToCheck):
                updateAccountDB(nameToCheck, passToCheck)
                return render_template("registered.html", username=nameToCheck)
            else:
                return returnInvalidInfo("register.html", "Username already taken")
        else:
            if passToCheck != passToCheck2:
                return returnInvalidInfo("register.html", "Passwords did not match")
            elif len(nameToCheck) > 16:
                return returnInvalidInfo("register.html", "Username must be 16 characters or less")
            elif len(passToCheck) < 9:
                return returnInvalidInfo("register.html", "Password must be 8 characters or more")
            else:
                return returnInvalidInfo("register.html", "Please enter an alphanumeric username/password")

@app.route("/login", methods=["POST", "GET"])
def login():
    nameToCheck = request.form.get("name")
    passToCheck = request.form.get("pass")
    correctInfo = checkLoginInfo(nameToCheck, passToCheck)
    if request.method == "GET":
        return render_template("login.html")
    else:
        if checkStringValid(nameToCheck) and checkStringValid(passToCheck):
            if correctInfo == True:
                return render_template("loggedin.html", username=nameToCheck)
            elif correctInfo == "No Account":
                return render_template("login.html", usernamealert="No existing account for username '{}'".format(nameToCheck))
            else:
                return render_template("login.html", usernamealert="Incorrect username/password")
        else:
            return returnInvalidInfo("login.html", "Please enter a valid (alphanumeric) username/password")
