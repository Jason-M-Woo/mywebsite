import psycopg2

DBNAME = "noobology"

def checkUsernameUnique(usernameToCheck):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select username from users where username = '{}';".format(usernameToCheck))
    name = c.fetchone()
    if name is None:
        return True
    else:
        return False
    db.close()

def checkLoginInfo(usernameToCheck, passwordToCheck):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select username from users where username = '{}';".format(usernameToCheck))
    name = c.fetchone()
    if name is None:
        return "No Account"
    d = db.cursor()
    d.execute("select password from users where username = '{}';".format(usernameToCheck))
    password = d.fetchone()
    if (passwordToCheck == password[0]):
        return True
    else:
        return False

    db.close()

def updateAccountDB(username, password):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("insert into users (username, password) values ('{}', '{}')".format(username, password))
    db.commit()
    db.close()
