import requests, json, os 
from requests.auth import HTTPBasicAuth #authenticates our credentials



CLIENT_ID = "dedf2f53ad924478af20048af3b30541"
CLIENT_SECRET = "3032aeedbea945649d474be2062df42e"

clientID = os.environ['CLIENT_ID'] #fonctionne pour replit, à reprendre
clientSecret = os.environ['CLIENT_SECRET']#fonctionne pour replit, à reprendre

url = "https://accounts.spotify.com/api/token" #adresse à laquelle se connecter

dico = {"grant_type" : "client_credentials"} #communique direct avec API : demande à Spotify de renvoyer infos d'identification à partir de ID et Secret

auth = HTTPBasicAuth(clientID, clientSecret) #envoie ID et Secret à Spotify ainsi que le nom d'utilisateur et le mot de passe pour connection

response = requests.post(url, data=dico, auth=auth) #stocke la clé API renvoyée par request qui envoie à Spotify les informations de connexion nécessaires.

url = "https://api.spotify.com/v1/search"

print( response.text )

accessToken = response.json()["access_token"] #recup token d'accès

headers = {'Authorization': f'Bearer {accessToken}'} #permet communication avec API via token"""

print(headers)

artist = input("Artiste : ") 

search = f"?q=artist%3A{artist}&type=track&limit=5"
fullURL = f"{url}{search}"

response = requests.get(fullURL, headers=headers)

#print(response.text)
data = response.json()

for track in data['tracks']['items']: #data["tracks"] pas reconnu / KeyError
  print(track["name"])