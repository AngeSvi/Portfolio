from flask import Flask, request, redirect, session
from replit import db
import os

sessionKey = os.environ["SECRET_KEY"] #fonctionne sur replit

app = Flask(__name__)
app.secret_key = "code"

@app.route('/')
def index():
    if session.get('loggedIn'):
        return redirect('/welcome')
    f = open("menu.html", "r")
    page = f.read()
    f.close()
    return page

@app.route('/signup', methods=["POST"])
def createUser():
    if session.get('loggedIn'):
        return redirect('/welcome')
    keys = db.keys()
    form = request.form()
    if form["username"] not in keys:
        db[form["username"]]={"username": form["username"], "password": form["password"]}
        return redirect("/login") 
    return redirect("/signup")

@app.route('/signup')
def signup():
    if session.get('loggedIn'):
        return redirect('/Welcome')
    page=""
    f = open("signup.html", "r")
    page = f.read()
    f.close()
    return page 

@app.route('/login', methods=["POST"])
def doLogin():
    if session.get('loggedIn'):
        return redirect('/welcome')
    keys = db.keys()
    form = request.form()
    if form["username"] not in keys:
        return redirect("/login") 
    else:
        if form["password"]==db[form["username"]]["password"]:
            session['loggedIn'] = form['username'] #session est un dictionnaire auquel on associe une clé 'loggedIn' (de valeur form['username'])
            return redirect('/welcome')
        else:
            return redirect("/login")

@app.route('/login')
def login():
    if session.get('loggedIn'):
        return redirect('/welcome')
    page=""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page 

@app.route('/welcome')
def welcome():
    page=f"""<h1>Hi there {db[session['loggedIn']]["name"]}</h1>
    <button type="button" onClick="location.href='/logout'>Log out</button>"""
    return page

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
     
app.run(app.run(host='0.0.0.0', port=81))
