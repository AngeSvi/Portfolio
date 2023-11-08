from flask import Flask, redirect, request
from replit import db
import os
from fonctions import *
from datetime import date, datetime
from datastore import *

sessionKey = os.environ["SECRET_KEY"] #fonctionne sur replit

db["admin"] = {"Lulu":"mdp_lulu", "Toto":"mdp_toto"}
db["users"] = {"Bob":"mdp", "Alice":"hatter"}

data = dataStore()

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']#donne clé pour pouvoir accéder aux infos dans session 

@app.route('/')
def index():
    """affiche le menu"""
    f = open('menu.html', 'r')
    page = f.read()
    page+="""</body>"""
    return page

@app.route('/login')
def login():
    """affiche la page login"""
    f = open('login.html', 'r')
    page = f.read()
    f.close()
    return page
    
@app.route('/login', methods=["POST"])
def logged():
    """vérifie que bien identifié"""
    if request.form['username'] in db["admin"].keys():
        if request.form['password'] == db["admin"][request.form['username']] :
            data.logged_user = request.form['username']
            return redirect('/userMenu')
    if request.form['username'] in db["users"].keys():
        if request.form['password'] == db["users"][request.form['username']] :
            data.logged_user = request.form['username']
            return redirect('/userMenu')
    return redirect('/')

@app.route('/userMenu', methods=['POST'])
def save():
    """modifie json pour y ajouter le nouveau message écrit""" 
    chat = loadjson()
    new_message = []
    new_message.append(f"/static/profil_pictures/{data.logged_user.lower()}.jpg")
    new_message.append(data.logged_user)
    new_message.append(request.form['message'])
    chat.append(new_message)
    savejson(chat)
    return redirect('/userMenu')
            
@app.route('/userMenu')
def userMenu():
    """affiche une page personnalisée en fonction de l'user"""
    g = open('usermenu.html', 'r')
    page = g.read()
    if data.logged_user in db["admin"]:
        #ajoute un button pour accéder à suppression
        page += """<form action="/adminMenu"><button type="onclick">Admin</button></form>"""
    conversation = loadjson()
    conversation.reverse()
    for message in conversation[0:5]: #affiche les 5 derniers messages
        page += """<h2>{username}</h2> 
        <img src={picture}>
        <p>{message}</p>"""
        page = page.replace("{picture}", message[0])
        page = page.replace("{username}", message[1])
        page = page.replace("{message}", message[2])
    page+="""</body>"""
    return page    

@app.route('/adminMenu')
def adminMenu():
    """page pour suppression"""
    if data.logged_user in db["admin"]:
        g = open('usermenu.html', 'r')
        page = g.read()
        conversation = loadjson()
        for numero_message in range(len(conversation)) :
            message = conversation[numero_message]
            page += """<form method="post" action="/deleteMessage">
            <h2>{username}</h2> 
            <img src={picture}>
            <p>{message}</p>"""
            page = page.replace("{picture}", message[0])
            page = page.replace("{username}", message[1])
            page = page.replace("{message}", message[2])
            page += f"""<button type="submit">Delete</button><input type="hidden" id="messageId" name="numero_message" value="{numero_message}"></form>"""
        page+="""</body>"""
    return page    

@app.route('/deleteMessage', methods=["POST"])
def deleteMessage():
    chat = loadjson()
    del chat[int(request.form['numero_message'])]
    savejson(chat)
    return redirect('/userMenu')

app.run(host='0.0.0.0', port=81)
