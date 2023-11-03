#fonctions
SCORE_ELIMINATOIRE = -10
MULTIPLICATEUR_CIBLE = 0.8

def trouve_joueur_le_plus_proche(players):
    """Vérifie quel joueur est le plus proche de la cible*0.8"""
    joueur_le_plus_proche = list(players.keys())[0]
    for player in trouver_joueurs_en_lice(players):
        if players[joueur_le_plus_proche]["difference"] > players[player]["difference"] :
            joueur_le_plus_proche = player
    return joueur_le_plus_proche

def calcul_difference_nombre_cible(players, cible):
    for player in players:
        number_choice = players[player]["number_choice"]
        players[player]["difference"] = abs(cible - number_choice)


def elimine_selon_score(players):
    copy_players = players.copy()
    for player in players:
        if players[player]["score"] <= SCORE_ELIMINATOIRE :
            print(f"""{player} a perdu. Il est éliminé.""")
            del(copy_players[player])
    return copy_players
    

def trouver_joueur_avec_meme_choix(players):
    joueurs_avec_meme_choix = set()
    for player1 in players :
        for player2 in players:
            if player1 != player2: #pour pas être comparé à soi-même
                if players[player1]["difference"] == players[player2]["difference"] :
                    joueurs_avec_meme_choix.add(player1)
                    joueurs_avec_meme_choix.add(player2)
    return joueurs_avec_meme_choix


    
def print_score(players):
    for player in players :
        print(f"""{player} : {players[player]["score"]}""")

def calcul_cible(players):
    somme_choix = 0
    for player in players :
        somme_choix += players[player]["number_choice"]
    cible = (somme_choix * MULTIPLICATEUR_CIBLE) / len(players)
    return cible

def verifie_100_0(players):
    list_number_choice = []
    for player in players:
        list_number_choice.append(players[player]["number_choice"])
    return 100 in list_number_choice and 0 in list_number_choice

def trouve_joueur_100(players):
    if players[list(players.keys())[0]]['number_choice'] == 100:
        return list(players.keys())[0]
    else : 
        return list(players.keys())[1]
    
def disqualifier_un_joueur(players, player):
    players[player]["disqualifier"] = True

def trouver_joueurs_en_lice(players):
    joueurs_en_lice = []
    for player in players:
        if not players[player]["disqualifier"] :
            joueurs_en_lice.append(player)
    return joueurs_en_lice


def cible_exacte_atteinte(players, cible):
    for player in trouver_joueurs_en_lice(players) :
        return players[player]["number_choice"] == cible


def resoudre_et_annoncer_la_perte_de_points(players, vainqueur, activer_mode_exact):
    point_en_jeu = 1
    if activer_mode_exact :
        point_en_jeu = 2
        print(f"""{vainqueur} a deviné le nombre exact. Tous ses adversaires perdent deux points.""")

    for player in players :
        players[player]["score"] -= point_en_jeu

    players[vainqueur]["score"] += point_en_jeu