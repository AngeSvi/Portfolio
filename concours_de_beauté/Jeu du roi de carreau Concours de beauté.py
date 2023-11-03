#Jeu du roi de carreau (Alice in Borderland)

from fonctions import *
import random

players = {
            "Jojo" : {"score" : 0, "number_choice" : 0, "difference" : 0, "disqualifier" : False},
            "Bob" : {"score" : 0, "number_choice" : 0, "difference" : 0, "disqualifier" : False},
            "Chishiya" : {"score" : 0, "number_choice" : 0, "difference" : 0, "disqualifier" : False},
            "Daya" : {"score" : 0, "number_choice" : 0, "difference" : 0, "disqualifier" : False},
            "Xmas_Georges" : {"score" : 0, "number_choice" : 0, "difference" : 0, "disqualifier" : False}
        }

activer_mode_exact = False
vainqueur_special = False

while len(players) != 1 : 
    
    for player in players :
        number_choice = 101
        while not 0<= number_choice <= 100:
            #number_choice = int(input(f"Choisissez un nombre entre 0 et 100 {player} > "))
            number_choice = random.randint(0, 100)
        players[player]["number_choice"] = number_choice

    """for player in players:
        somme_choix += players[player]["number_choice"]"""
    
    cible = round(calcul_cible(players))
    
    print(f"""La cible des nombres choisis par l'ensemble des joueurs est de {cible}.""")

    calcul_difference_nombre_cible(players, cible)

    if len(players) < 5:
        joueur_avec_meme_choix = trouver_joueur_avec_meme_choix(players)
        if len(joueur_avec_meme_choix) > 0 :
            print("Plusieurs joueurs ont choisi le même nombre. Ils perdent chacun un point.")
        for player in joueur_avec_meme_choix :
            print(f"""{player} perd un point.""")
            disqualifier_un_joueur(players, player)

    if len(players) < 4:
        # Si la cible est trouvée exactement, 2 points sont en jeu
        activer_mode_exact = cible_exacte_atteinte(players, cible)      
                    
    if len(players) == 2 :
        active_regle_speciale = verifie_100_0(players)
        if active_regle_speciale :
            vainqueur_special = trouve_joueur_100(players)
            
  
    if vainqueur_special:
        vainqueur = vainqueur_special
    else :
        vainqueur = trouve_joueur_le_plus_proche(players)

    resoudre_et_annoncer_la_perte_de_points(players, vainqueur, activer_mode_exact)

    players = elimine_selon_score(players)
    print_score(players)

print(f"""Tous vos adversaire ont été éliminés {list(players.keys())[0]}. Félicitations, vous remportez la partie.""")


#faire une annonce de règle quand un joueur est éliminé 
#nettoyage
#bot discord ?
#base de données pour stocker