import random

def tocaractere (liste):
    new_caractere = ""
    for elt in liste :
        new_caractere += elt + " "
    return new_caractere

bagel = []

i = 0 
while i < 3 :
    n = random.randint(1, 9)
    if str(n) not in bagel :
        bagel.append(str(n))
        i += 1 

affiche = []

print("You'll try to guess the secret number this computer chose. It gives you three types of clues : \n - If none of the three digits guessed is in the secret number, it will say \"\033[32mBagels\033[0m\".\n - If one of the digits is in the secret number, but the guess has the digit in the wrong place, it will be \"\033[33mPico\033[0m\".\n - Finally, if he guess has a correct digit in the correct place, it's a \"\033[34mFermi\033[0m\" !.\nA number can't be founded more than one time in the secret number.\n")


while affiche != ["Fermi", "Fermi", "Fermi"] :
    affiche = []
    affiche_bagel = []

    guess = list(input("\nTry to guess the secret number > "))
    
    for number in guess : 
        if number in bagel :
            if guess.index(number) == bagel.index(number):
                affiche.append("Fermi")
            else :
                affiche.append("Pico")
        else : 
            affiche_bagel.append("Bagels")
            
    if affiche_bagel == ["Bagels", "Bagels", "Bagels"] :
        print("Bagels")
    elif affiche == ["Fermi", "Fermi", "Fermi"] :
        print(f"You win, the secret number was {tocaractere(bagel)}")
    else : 
        affiche = tocaractere(sorted(affiche))
        print(affiche)

#Ajouter voulez-vous rejouer 