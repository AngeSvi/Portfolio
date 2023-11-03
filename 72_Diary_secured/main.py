from replit import db
import datetime, os, time
import random

username = input("Create an username > ")
password = input("Create a password > ")
salt = random.randint(1000, 9999)
newPassword = f"{password}{salt}"
newPassword = hash(newPassword)

db[username] = {"password": password, "salt": salt}

while True :
    inputUsername = input("Input username > ")
    keys = db.keys()
    
    if inputUsername not in keys :
        print("Unknown")
        
    else :
        inputPassword = input("Input password > ")
        inputPassword = f"{inputPassword}{salt}"
        inputPassword = hash(inputPassword)
        
        if inputPassword != newPassword :
            print ("Wrong password")
    
        else :
            print("Welcome in your diary")
            time.sleep(1)
            while True :
                menu = input("Diary menu - 1) Add 2) View 3) Exit > ")
                os.system("clear")
                
                if menu == "1":
                    timestamp = f"date - {datetime.datetime.now()}"
                    secret = input(f"{timestamp} : ")
                    db[timestamp] = secret
                    
                elif menu == "2" :
                    matches = db.prefix("date")
                    i = 0
                    for elt in matches :
                        print(db[matches[i]])
                        i += 1
                        next = input("Next secret ? > ").lower()
                        if next.startswith("n") :
                            break
                            
                elif menu == "3" :
                    print("Diary closed.")
                    break
        
                else :
                    print("Wrong input, try again.")
                    continue