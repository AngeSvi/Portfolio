import random
import os, time


def affichage_grille (cases):
    """affiche la grille de morpion"""
    print(f" {cases[7]} | {cases[8]} | {cases[9]}")
    print("---+---+---")
    print(f" {cases[4]} | {cases[5]} | {cases[6]}") 
    print("---+---+---")
    print(f" {cases[1]} | {cases[2]} | {cases[3]}")

def qui_commence ():
    """Fonction qui tire à pile ou face celui qui commence"""
    piece = random.randint(1, 2)
    if piece == 1 : 
        print ("C'est au joueur de commencer.")
    else :
        print ("C'est à l'ordinateur de commencer.")
    return piece 


def choix_symbole():
    """Fonction qui attribue les symboles"""
    while True : 
        choix_joueur = input ("Souhaitez-vous jouer les X ou les O ? ").strip().upper()
        if choix_joueur == "X":
            symbole_pc = "O"
            return choix_joueur, symbole_pc
        elif choix_joueur == "O":
            symbole_pc = "X"
            return choix_joueur, symbole_pc
        else :
            continue

cases = {
    1 : " ", 
    2 : " ", 
    3 : " ", 
    4 : " ", 
    5 : " ", 
    6 : " ", 
    7 : " ", 
    8 : " ", 
    9 : " "
}

possibilites = ['1', '2', '3', '4', '5', '6', '7', '8', '9']   

def victoire (symbole, grille):
    """renvoie combinaison de cases gagnantes"""
    return grille[1] == grille[2] == grille[3] == symbole \
        or grille[4] == grille[5] == grille[6] == symbole \
        or grille[7] == grille[8] == grille[9] == symbole \
        or grille[7] == grille[4] == grille[1] == symbole \
        or grille[8] == grille[5] == grille[2] == symbole \
        or grille[9] == grille[6] == grille[3] == symbole \
        or grille[7] == grille[5] == grille[3] == symbole \
        or grille[1] == grille[5] == grille[9] == symbole
        
def grille_liste(cases):
    """transforme la grille de morpion en liste de ' ', de X et de O"""
    liste = []
    for number, value in cases.items() :
        liste.append(value)
    return liste
    
continuer = ["OUI", "O"]

def randomMouv (cases, listMouv): #listMouv diffère pour les coins, les côtés ... 
    """indique à l'ordinateur les cases qu'il peut occuper"""
    mouvementsPossibles = []
    for i in listMouv :
        if cases[i] == " ":
            mouvementsPossibles.append(i)
    if len(mouvementsPossibles) != 0 : #s'il reste des cases à occuper
        return random.choice(mouvementsPossibles)
    else : 
        return None

def pc_mouvement(cases, symbole_pc, symbole_jo):
    """définit les mouvements de l'ordinateur lorsqu'il joue"""

    for mouvement in range(1, 10):
        test_cases = cases.copy() #copie de la grille actuelle
        if test_cases[mouvement] == ' ': #est-ce que libre ? 
            test_cases[mouvement] = symbole_pc #place symbole_pc 
            mouvementGagnant = victoire(symbole_pc, test_cases) #vérifie la victoire 
            if mouvementGagnant: 
                return mouvement
                 
    #bloque mouvement du joueur pour l'empêcher de gagner 
    for mouvement in range(1, 10):
        test_cases = cases.copy()
        if test_cases[mouvement] == ' ': 
            test_cases[mouvement] = symbole_jo
            mouvementGagnant = victoire(symbole_jo, test_cases)
            if mouvementGagnant : #si le mouvement est gagnant pour le joueur, le pc lui vole
                return mouvement
    
    #essaye d'occuper un coin si libre 
    mouvement = randomMouv(cases, [1, 3, 7, 9])
    if mouvement != None : #s'il y a bien une case à occuper
        return mouvement

    else : 
        #essaye d'occuper le centre 
        mouvement = randomMouv(cases, [5])
        if mouvement != None : #s'il y a bien une case à occuper 
            return mouvement

        else :
            #occupe les côtés
            return randomMouv(cases, [2, 4, 6, 8])

#______________________________

os.system("clear")
nouvelle_partie = "OUI"
while nouvelle_partie in continuer :
    symbole_jo, symbole_pc = choix_symbole()
    first = qui_commence()
    while not victoire(symbole_jo, cases) and not victoire(symbole_pc, cases):
        
        os.system("clear")
        affichage_grille(cases) 
    
        if ' ' not in grille_liste(cases):
            print("Match nul")
            break 
            
        if first % 2 == 1 : #impair donc au joueur de jouer 
            print ("C'est au tour du joueur")
            mouvement = ' '
            while mouvement not in possibilites :
                mouvement = input("Prochain mouvement : ")
                
            possibilites.remove(mouvement)
            mouvement = int(mouvement)
            # Verifier que mouvement est possible
            cases[mouvement] = symbole_jo
            first += 1

        else : #pair donc à la machine de jouer 
            print("C'est au tour de l'ordinateur")
            mouvement = pc_mouvement(cases, symbole_pc, symbole_jo)
            cases[mouvement] = symbole_pc
            possibilites.remove(str(mouvement))
            first += 1 
            time.sleep(1)

    affichage_grille(cases) #affiche la grille avec le dernier symbole qui donne la victoire (sinon apparaît pas)
    nouvelle_partie = input("Voulez-vous jouer une nouvelle partie ? ").strip().upper()
    if nouvelle_partie not in continuer :
        print("Fin de la partie")
        break