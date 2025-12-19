""" Calculatrice """

"""
a = b =""

while not (a.isdigit() and b.isdigit()):
    a = input ("Veuillez entrer un premier nombre : ")
    b = input ("Veuillez entrer un deuxième nombre : ")

    if not (a.isdigit() and b.isdigit()):
        print ("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} et {b} est {int(a) + int(b)}")

"""

""" Liste de courses """
"""
liste_course=[]

choice = input (" Choisissez parmi les 5 options suivantes: " \
"1 : Ajouter un élément à la liste" \
"2 : Retirer un élément de la liste" \
"3 : Afficher la liste" \
"4 : Vider la liste" \
"5 : Quitter" \
"👉 Votre choix : ")

while True : 
    if choice == "1" :
        ajout = input("Quel produit souhaitez-vous ajouter : ")
        liste_course.append(ajout)
        
    elif choice == "2" : 
        retrait = input ("Quel produit produit souhaitez-vous retirer : ")
        if retrait in liste_course:
            liste_course.remove(retrait)
        else:
            print("Ce produit n'est pas dans la liste")
        
    elif choice == "3" : 
        print("Voici votre liste de course: ", liste_course)
        
    elif choice == "4" :
        liste_course.clear()
        print ("Liste de course vidée")
        
    elif choice == "5": 
        print ("A bientôt")
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

    """

""" Le nombre mystère """

import random

nombre_mystere= random.randint(0,100)
tour=5

while True:
    nombre_utilisateur= input("Deviner le nombre mystère : ")

    if not nombre_utilisateur.isdigit(): 
        print("Veuillez entrer un nombre valide")
    
    elif int(nombre_utilisateur)<0 or int(nombre_utilisateur)>100 :
        print("Veuillez entrer un nombre entre 0 et 100")

    else: 
        if int(nombre_mystere)>int(nombre_utilisateur) and tour>0:
            print(f"Le nombre mystère est plus grand que {nombre_utilisateur}")
            tour-=1
            print(f"Il vous reste {tour} essai{'s' if tour>1 else ''}")

        elif int(nombre_mystere)<int(nombre_utilisateur) and tour>0:
            print(f"Le nombre mystère est plus petit que {nombre_utilisateur}")
            tour-=1
            print(f"Il vous reste {tour} essai{'s' if tour>1 else ''}")

        elif int(nombre_mystere)==int(nombre_utilisateur) and tour>0 : 
            print(f"Bravo le nombre est bien {nombre_mystere}")
            print(f"Tu as trouvé la solution en {5-tour} essai{'s' if tour>1 else ''}")
        
        elif tour == 0:
            print(f"Perdu ! Le nombre mystère été : {nombre_mystere}")
            break

nombre_utilisateur= input("Deviner le nombre mystère : ")
