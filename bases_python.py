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
    resultat= a/b
exept ZeroDivisionError:
    print("La division par zéro n'est pas possible")

sinon par exemple si b = "bonjour"

exept TypeError as e: 
    print ("Erreur: ", e) --> on print le type d'erreur

on peut ajouter une variable else, il ne sera executer que si le try réussi:

else: 
    print (resultat)

on peut egalement mettre un bloc finally qui s'executera quoiqu'il se passe: 

finally:
    print("bloc terminé")

""" 
""" 
On peut créer des modules et les importer avec import mon_module
Appeller ensuite une variable contenu dans le module avec mon_module.variable

Utiliser le  python path pour créer des chemins. Sys

Les packages :
    a chaque fois que le package est importé le fichier __init__ sera lu.

Les formats docstring

    syntaxe de google : 
        Args:
            param1: un premier paramètre
            param2: un deuxième paramètre

        Returns: 
            description de ce qui est retourné

"""

def fonction_onsenfou (nom, age):
    """_summary_       

    Args:
        nom (str): nom de l'utilisateur
        age (int): age de l'utilisateur

    Returns:
        list: list de nombre
    """
    return [1,2,3]



import logging

logging.basicConfig(level=logging.DEBUG, # permet de configurer de le logging sinon par défaut les seuls qui seront configuré seront warning, error et critical.
#ATTENTION avec cette commande ce sont tous les niveaux de logging à partir du DEBUG qui vont affichés. Ici --> Tous. Donc l'ordre d'affichage à son importance. S'il été en deuxième ligne, info ne se configurerai pas.
                    filename="app.log" #nom du fichier dans lequel ont veut mettre les alerte
                    filemode="w" #w (write) si on veut écraser, a (append) si on veut ajouter
                    format='%(asctime)s - %(levelname)s -%(message)s')

logging.debug("La fonction a bie nété exécuté")
logging.info ("Message d'information générale") #informe à l'utilisateur que son action a bien réussie
logging.warning("Attention!") #avertissement qui ne fera pas planter le script. Non critique
logging.error("une erreur est arrivée") #un peu plus qu'un avertissement, tj pas critique, le script peut continuer de fonctionner. Juste une étape du script n'a pas fonctionné
logging.critical('Erreur critique') #le script plantera


""" CREER UN ENVIRONNEMENT VIRTUEL """

"""
    dans bash créer un mkdir mon_projet
    ensuite python m- venv nom_de_environnement_virtuel exemple env
    ls pour voir les sous dossier
    cd Scripts
    sources activate --> la on doit voir un (env) qui apparait pour dire qu'on est dans l'environnement virtuel
    deactivate pour désactiver. 

    Pour les Pip: 
    dans bash taper pip3.13 (selon la version de Python)

    aller voir pypi.org pour voir toutes les librairies qu'on peut installer. Ex request... sinon on peut chercher la commande search pour rechercher les modules. 

    Installer les packages : 
        

"""



