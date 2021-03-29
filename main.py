import requests

respons = requests.get("https://www.ceneo.pl/70068802#tab=reviews")
print(respons.text)