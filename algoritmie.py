import string

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
phrase=lorem.lower().replace(".","").replace(",","").replace(" ","")

alphabet = list(string.ascii_lowercase)

compteur={}

for lettre in phrase:
    if lettre.isalpha():
        compteur[lettre]=compteur.get(lettre, 0) +1

resultat=dict(sorted(compteur.items()))

print(resultat)