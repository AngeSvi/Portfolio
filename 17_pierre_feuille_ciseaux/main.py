from getpass import getpass as input #entrée invisible
from fonctions import *

print("Pierre feuille ciseaux")
print("Quels sont les noms des joueurs ?")
NJ1 = str(input("Nom du joueur 1 > "))
NJ2 = str(input("Nom du joueur 2 > "))

joueurs = {
            NJ1 : {"nom" : NJ1, "score" : 0, "geste" : "x"},
            NJ2 : {"nom" : NJ2, "score" : 0, "geste" : "x"},
    }

score1 = 0
score2 = 0

continuer = "oui"

while continuer == "oui":

    joueurs[NJ1]["geste"], joueurs[NJ2]["geste"] = choix_du_geste(NJ1, NJ2)

    if J1 == "P":
        if J2 == "P":
            print("Égalité !")
        elif J2 == "F":
            print({NJ2}, "emballe la pierre de", NJ1, ", victoire de", {NJ2}, " !")
            score2 += 1
        elif J2 == "C":
            print(f"Les ciseaux de {NJ2} sont réduits en miettes par la pierre de {NJ1}, victoire de {NJ1} !")
            score1 += 1
        else:
            print("Faux mouvement ", {NJ2}, ", réessayez.")
    elif J1 == "F":
        if J2 == "P":
            print({NJ1}, " enroule la pierre de ", {NJ2}, ", victoire de ", {NJ1},
                  " !")
            score1 += 1
        elif J2 == "F":
            print("Egalité !")
        elif J2 == "C":
            print("Les ciseaux de ", {NJ2}, " découpent la feuille de ", {NJ1},
                  ", victoire de ", {NJ2}, " !")
            score2 += 1
        else:
            print("Faux mouvement ", {NJ2}, ", réessayez.")
    elif J1 == "C":
        if J2 == "P":
            print({NJ2}, "écrabouille les ciseaux de ", {NJ1}, ", victoire de ",
                  {NJ2}, " !")
            score2 += 1
        elif J2 == "F":
            print("Le ", {NJ1}, " fait des confettis de la feuille de ", {NJ2},
                  ", victoire du ", {NJ1}, " !")
            score1 += 1
        elif J2 == "C":
            print("Egalité !")
        else:
            print("Faux mouvement ", {NJ2}, ", réessayez.")
    else:
        print("Faux mouvement ", {NJ1}, ", réessayez.")
    
    continuer = input("Voulez-vous rejouer une partie ? ")

    else:
        

#comment désigner qui a pris quoi

def qui_a_gagne(joueurs):
    print(f"La partie est terminée ! \n{joueurs[NJ1]["nom"]} a {joueurs[NJ1]["score"]} points 
          et {joueurs[NJ2]["nom"]} {joueurs[NJ2]["score"]} points.")
    
    scores = [joueurs[NJ1]["score"], joueurs[NJ2]["score"]]

    
    
    if {joueurs[NJ1]["score"]} > {joueurs[NJ2]["score"]}
        print("C'est", {NJ1}, "qui remporte la partie !")
        break
    elif score1 == score2:
        print("Vous êtes à égalité, c'est un match nul")
        break
    else:
        print("C'est", {NJ2}, "qui remporte la partie !")
        break

