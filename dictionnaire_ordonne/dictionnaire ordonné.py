class dicordo():
        def __init__(self):
            pass
        def __getitem__(self, item):
            return self.__dict__[item]
        def __setattr__(self, key, value):
            """Méthode appelée quand fait objet.key = value"""
            self.__dict__[key] = value
            print("On ajoute {0} {1}s dans le dictionnaire".format(value, key))
        def __setitem__(self, key, value):
            self.__dict__[key] = value
            print("On ajoute {0} {1}s dans le dictionnaire".format(value, key))
        def __repr__(self):
            """Quand on entre notre objet dans l'interpréteur"""
            return str(self.__dict__)
        def __contains__(self, key):
            return key in self.__dict__
        def __len__(self):
            return len(self.__dict__)
        def __tri__ (self, value):
            return sorted(self.__dict__)




fruits = dicordo()
fruits.pomme = 59
print (fruits.__dict__)
fruits.cerise = 12
print (fruits)
fruits["peche"] = 22
print (fruits)
print ('haricot' in fruits)
print(len(fruits))
fruits.__tri__()