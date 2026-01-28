mot = "un roc cornu"

lettres = mot.replace("", " ")
liste=lettres.lower().split()

if liste == liste[::-1]:
    resultat=True
else:
    resultat=False

print(resultat)