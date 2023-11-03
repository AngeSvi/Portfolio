from flask import request, redirect
import json

def tri(liste_entree):
    liste_sortie = [] #liste vide pour accueillir le + petit elt liste à trier -> supprimer au fur et à mesure dans liste_entree
    copy_liste = liste_entree[:] #copie liste pour pas endommager la variable
    while len(copy_liste) != 0: #Tant qu'il reste des éléments à trier
        ppelt = copy_liste[0]
        for elt in copy_liste:
            if elt[0] > ppelt[0]:
                ppelt = elt
        liste_sortie.append(ppelt)
        copy_liste.remove(ppelt)
    return liste_sortie

def loadjson():
    with open("publications.json", "r") as jsonfile :
        json_data = json.load(jsonfile)
        return json_data["data"]

def savejson(data):
    dico = {"data" : data} #ce qui va être ajouté 
    with open("publications.json", "w") as jsonfile :
        json.dump(dico, jsonfile)
#prend en paramètres les données à enregistrer dans le fichier json