import requests, json
from replit import db

autorised_answers = ["s", "l", "n"]

while True :
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
    joke = result.json()
    print(f"""\n{joke["joke"]}""")

    action = ""
    while action not in autorised_answers:
        action = input("\n(s)ave joke, (l)oad joke or (n)ew joke ? > ").lower()

    if action == "s":
        "enregistre la blague dans db"
        db[f"""{joke["id"]}"""] = joke["joke"]
        print("\nJoke saved !\n")

    elif action == "l":
        for key in db.keys():
            print(f"""°{db[key]}""")