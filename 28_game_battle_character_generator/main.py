import random
import os
import time

def randomdice (side) :
    score = random.randint(1, side)
    return score 

def character_health ():
    character_health = (randomdice(6) * randomdice(12)) / 2 + 10 
    return character_health 

def character_strenght ():
    character_strenght = (randomdice(6) * randomdice(12)) / 2 + 12 
    return character_strenght

def character():
    name = input ("Name your legend :")
    race = input ("Character type (Human, Elf, Wizard, Orc) :")
    health = character_health()
    strenght = character_strenght()
    print (name,",", race, "\nHEALTH :", health, "\nSTRENGHT :", strenght)
    print () 
    character = {"name" : name, "race" : race, "health" : health, "strenght" : strenght}
    return character
    

def challenger ():
    p1 = character()
    print ("Who are they battling ?")
    p2 = character()
    time.sleep(4)
    #os.system("clear")
    print()
    return p1, p2 

def battle(toto, tati):
    damage = abs(toto["strenght"] - tati["strenght"]) + 1 
    dice_player_1 = randomdice(6)
    dice_player_2 = randomdice(6)
    score = dice_player_1 - dice_player_2
    if score > 0 :
        print (toto["name"], "wins that round ! Now", tati["name"], "'s life is", new_life(tati, damage), "HP !")
    elif score < 0 :
        print (tati["name"], "wins that round ! Now", toto["name"], "'s life is", new_life(toto, damage), "HP !")
    else :
        print ("Ex aequo !")
    print (toto["name"], "health : ", toto["health"])
    print (tati["name"], "health : ", tati["health"])
    time.sleep(4)
    #os.system("clear")

def new_life (victim, one_punch):
    victim["health"] = victim["health"] - one_punch
    return victim["health"]
#__________________

print ("BATTLE TIME")
player_1, player_2 = challenger()
while True :  
    print ("The battle begins!")
    battle(player_1, player_2)
    if player_1["health"] <= 0:
        print (player_1["name"], "is destroyed,", player_2["name"], "wins !")
        break
    elif player_2["health"] <= 0:
        print (player_2["name"], "is destroyed,", player_1["name"], "wins !")
        break