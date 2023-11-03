import random
import os 
import time

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "downton"]
yes = ["YES", "Y"]

wordChosen = [*random.choice(listOfWords)] #transforme mot en liste de lettres

new_game = "Y"
while new_game in yes :
    alphabet = []
    t = 5
    win = False 
    while win is False :
        
        if t == 0 :
            print ("Hangman")
            break
            
        else : 
            print("\nalphabet :", ''.join(alphabet), sep = " ")
            letter = input("\n\nChoose a letter : ").lower()
            if letter in alphabet :
                print("Tried yet")
                continue
    
            elif letter not in wordChosen:
                print ("\nNope")
                alphabet.append(letter)
                t -= 1
                print("You've got", t, "lives yet !")   
    
            else :
                win = True 
                alphabet.append(letter)
                print(" ")
                for letter in wordChosen :
                    if letter in alphabet : 
                        print(letter, end="")
                    else:
                        print("_", end="")
                        win = False
            time.sleep(1)
            os.system("clear")

    new_game = input("\nDo you want to play again? ").upper()