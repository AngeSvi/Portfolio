def weather_code_print(elt, to_append, list_to_print):
    """tri ce qui doit être mis dans les listes d'éléments à afficher"""
    if elt not in list_to_print :
        list_to_print.append(to_append)

def max_temperature(temperature_liste, temperature_comparated):
    if temperature_liste[0] < temperature_comparated :
        temperature_liste = [temperature_comparated]
        return temperature_liste

def min_temperature(temperature_liste, temperature_comparated):
    
        return temperature_liste
