import requests, json
from fonction import *
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=2))

cloudy = ["0, ""1", "2", "3", "4"]
sandorsmoke = ["5", "6", "7", "8", "9"]
fogprecipitation = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]
rainorsnow = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
storm = ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39"]
icefog = ["40", "41", "42", "43", "44", "45", "46", "47", "48", "49"]
precipitation = ["50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]

i = range(len(user["daily"]["weathercode"]))
code_print = []

for elt in i :
    code = str(user["daily"]["weathercode"][elt])
    weather_code_print(code, code, code_print)

final_print = []

for elt in code_print :
    if elt in cloudy:
        elt = "Cloudy"
        weather_code_print(elt, elt, final_print)

    elif elt in sandorsmoke:
        elt = "Reduced visibility"
        weather_code_print(elt, elt, final_print)

    elif elt in fogprecipitation:
        elt = "Fog or precipitation"
        weather_code_print(elt, elt, final_print)

    elif elt in rainorsnow:
        elt = "Rain or snow"
        weather_code_print(elt, elt, final_print)

    elif elt in storm:
        elt = "Storm"
        weather_code_print(elt, elt, final_print)
    
    elif elt in precipitation:
        elt = "Precipitations"
        weather_code_print(elt, elt, final_print)

for elt in final_print :
    print(elt)

temperature_max = user["daily"]["temperature_2m_max"][0]
temperature_min = user["daily"]["temperature_2m_min"][0]

max_range = range(len(user["daily"]["temperature_2m_max"]))
min_range = range(len(user["daily"]["temperature_2m_min"]))

for elt in max_range :
    releve_temp_max = user["daily"]["temperature_2m_max"][elt]
    if temperature_max < releve_temp_max :
        temperature_max = releve_temp_max

for elt in min_range :
    releve_temp_min = user["daily"]["temperature_2m_min"][elt]
    if temperature_min > releve_temp_min :
        temperature_min = releve_temp_min

print(f"""🥵 : {temperature_max}    🥶 : {temperature_min}""")