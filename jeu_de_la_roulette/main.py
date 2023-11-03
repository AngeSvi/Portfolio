from errorless import errorless 
from game import game 
import os 

affirmatif = ["OUI", "YES"]

print ("Le jeu de la roulette\n")
continuer = "OUI"
bourse = 100
while continuer.upper() in affirmatif :
    case_misee, mise = errorless(bourse)
    bourse = game(bourse, case_misee, mise)
    if bourse == 0 :
        print("Votre bourse est vide ! Vous devriez aller retirer ou sortir de ce casino ...")
        print ("Perdu !")
        break
    continuer = input("Voulez-vous continuer la partie ?\n")
        
    
#voulez-vous continuer ? 
#changer les couleurs 
#clear l'interface 
#rajouter possiblités (miser sur moitié basse, sur plusieurs cases, tiers, couleurs ... comme dans dragon quest)
#enregistrer les scores 
