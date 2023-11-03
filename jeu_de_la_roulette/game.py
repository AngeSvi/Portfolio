import random
import math 

def game (bourse, case_misee, mise):
    """Déroulé de la partie"""
    case_obtenue = random.randrange(51)
    print(f"Le numéro gagnant est le {case_obtenue} !")
    if case_obtenue == case_misee:
        bourse *= 3
        print(f"Vous remportez la mise ! Votre bourse contient désormais {bourse}$.")
    elif case_misee % 2 == case_obtenue % 2 :
        bourse = bourse + math.ceil(mise / 2)
        if case_misee % 2 == 0 : 
            couleur = "rouge"
        else : 
            couleur = "noire"
        print(f"Vous aviez misé sur une case {couleur} de la même couleur que la case gagnante ! Vous remportez {math.ceil(mise / 2)}$. Votre bourse contient désormais {bourse}$.")
    else:
        bourse -= mise
        print(f"Vous avez perdu, dommage ... Votre bourse contient désormais {bourse}$.")
    return bourse 