""" Calculatrice """

a = b =""

while not (a.isdigit() and b.isdigit()):
    a = input ("Veuillez entrer un premier nombre : ")
    b = input ("Veuillez entrer un deuxième nombre : ")

    if not (a.isdigit() and b.isdigit()):
        print ("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} et {b} est {int(a) + int(b)}")
#print ("Voulez-vous faire un autre calcul? Y/N")

""" Liste de courses """

liste_courses=[]

choice = input (" Choisissez parmi les 5 options suivantes: " \
"1 : Ajouter un élément à la liste de courses" \
"2 : Retirer un élément de la liste de courses" \
"3 : Afficher la liste de courses" \
"4 : Vider la liste de courses" \
"5 : Quitter" \
"👉 Votre choix : ")

while True : 
    if choice == "1" :
        ajout = input("Quel produit souhaitez-vous ajouter : ")
        liste_courses.append(ajout)
        
    elif choice == "2" : 
        retrait = input ("Quel produit produit souhaitez-vous retirer : ")
        if retrait in liste_courses:
            liste_courses.remove(retrait)
        else:
            print("Ce produit n'est pas dans la liste")
        
    elif choice == "3" : 
        print("Voici votre liste de course: ", liste_courses)
        
    elif choice == "4" :
        liste_courses.clear()
        print ("Liste de course vidée 🛒❌")
        
    elif choice == "5": 
        print ("A bientôt 👋")
        break

    else : 
        print ("Votre choix ne correspond à aucune option")

    choice = input (" Choisissez parmi les 5 options suivantes: " \
    "1 : Ajouter un élément à la liste" \
    "2 : Retirer un élément de la liste" \
    "3 : Afficher la liste" \
    "4 : Vider la liste" \
    "5 : Quitter" \
    "👉 Votre choix : ")


""" Le nombre mystère """

import random

nombre_mystere= random.randint(0,100)
tour=5

while tour>0 :
    print(f"il vous reste {tour} essai{'s' if tour>1 else ''}")

    nb_utilisateur=input("Devinez le nombre: ")
    

    if not nb_utilisateur.isdigit():
        print("Veuilllez entre un nombre entre 0 et 100")
        continue
    elif int(nb_utilisateur)>100 or int(nb_utilisateur)<0:
        print("Veuilllez entre un nombre entre 0 et 100")
        continue

    nb_utilisateur=int(nb_utilisateur)

    if nb_utilisateur>nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nb_utilisateur}")
    elif nb_utilisateur<nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nb_utilisateur}")
    else:
        break

    tour-=1

if tour==0 :
    print(f"Trop tard! ⏳ Le nombre mystère été {nombre_mystere}") 

if tour>0 and nb_utilisateur==nombre_mystere: 
    print(f"Félicitation 🎉 le nombre mystère est bien {nb_utilisateur}. Tu as réussi en {5 - tour}  essais 🚀")
    



""" Jeu de rôle"""
import random

pv_joueur=50
pv_adversaire=50

nb_potions=3


while pv_joueur>0 and pv_adversaire>0: 
    choix=input('Souhaitez-vous attaquer "1" ou utiliser une potion "2" : ')

    if choix!="1" and choix!="2":
        continue
    elif not choix.isdigit():
        continue

    attaque_joueur=random.randint(5,10)
    attaque_adv=random.randint(5,15)

    if choix=="1" :
        print(f'Vous avez infligé {attaque_joueur} dégats à votre adversaire')
        print(f'Votre adversaire vous a infligé {attaque_adv} dégats')
        pv_joueur-=attaque_adv
        pv_adversaire-=attaque_joueur
        
    
    elif choix=="2":
        if nb_potions<=0:
                print("Vous n'avez plus de potions")
                continue
        
        potions=random.randint(15,50)
        nb_potions-=1

        print(f'Vous avez récupéré {potions} points de vie ❤️. Il ne vous reste plus que {nb_potions} potions 🧪')
        print(f'Votre adversaire vous a infligé {attaque_adv} dégats')
        pv_joueur=pv_joueur + potions - attaque_adv
        
    pv_joueur_aff=max(pv_joueur,0)
    pv_adversaire_aff=max(pv_adversaire,0)
    print(f'Il vous reste {pv_joueur_aff} points de vie 💔')
    print(f'Il reste {pv_adversaire_aff} points de vie à votre adversaire 💔')
    
if pv_joueur<=0: 
    print("Vous n'avez plus de point de vie 💀 ")

elif pv_adversaire<=0: 
    print("Vous avez vaincu votre adversaire 💪 ")

else: 
     print("Double KO 💀💀")
    


"""Mes fichiers JSON"""

"""
import json

with open ("data.json", "r") as f:  (r = read)
    json.load(f) = méthode pour lire les données dans le fichier

    de là on peut écrire donnees = json.load(f) --> on sauvegarde les données dans une variable 

    donnees.append(4) --> permet d'ajouter un élément à la liste

with open ("data.json", "w") as f:  (w = write)
    json.dump(donnees, f, indent=4) --> écrase les précédentes données donc la liste initiale, puis ajoute la nouvelle variable "donnée" incrémentée de (4) dans le f (fichier). Indent= 4 signifie juste qu'il y aura une indentation de 4 pour que ce soit plus lisible. 

    ajouter le paramètre ensure_ascii=False --> Sinon les accents ne s'affiche pas dans les données JSON; ATTENTION -> n'a aucun impact sur la lecture du fichier si on oublie. 

with open ("data.json", "a") as f:  (a = append)

"""

"""
La gestion des erreur:

LBYL et EAFP

Dans le second cas: try/exept

Exemple: 

a=5
b=0

si on cherche à print la division de a/b on aura une erreur de type "ZeroDivisionError" donc on 
try :
    a/b
exept ZeroDivisionError:
    print("La division par zéro n'est pas possible")

    


"""