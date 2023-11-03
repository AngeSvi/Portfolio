def choix_du_geste(joueur_1, joueur_2) :
    print("Choisissez pierre (P), feuille (F) ou ciseaux (C)")
    J1 = input(f"{NJ1} > ").upper()
    J2 = input(f"{NJ2} > ").upper()
    return J1, J2
