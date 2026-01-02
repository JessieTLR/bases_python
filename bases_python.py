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
    

