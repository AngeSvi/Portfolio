def errorless(bourse):
    """Empêche les erreurs d'entrée"""
    while (bourse > 0):
        print(f"Vous avez {bourse}$ dans votre bourse. Vous pouvez miser sur une case entre 0 et 49.")
        
        case_misee = -1
        while (not (type(case_misee) == int and 0 <= case_misee <= 49)):
            case_misee = input("Sur quelle case souhaitez-vous miser ?\n\n")
            try:
                case_misee = int(case_misee)
                assert 0 <= case_misee <= 49
            except ValueError:
                print("Vous devez saisir une valeur chiffrée")
            except AssertionError:
                print("Le numéro de la case sur laquelle vous souhaitez miser doit être compris entre 0 et 49 inclus.")
                
        mise = -1
        while (not (type(mise) == int and 0 < mise <= bourse)):
            mise = input("Quelle somme souhaitez-vous miser ?\n")
            try:
                mise = int(mise)
                assert bourse >= mise > 0
            except ValueError:
                print("Vous devez saisir une valeur chiffrée.")
            except AssertionError:
                print(f"Votre mise doit être supérieure à 0$ et ne peut pas excéder le montant de votre bourse, qui s'élève à {bourse}$.")
        return case_misee, mise
    
#modifier le montant de la bourse quand mise effectuée 