import random

nombre_mystere=random.randint(1,40)
tour=8

while tour>0:
    nombre=int(input("Choississez un nombre entre 0 et 100"))
    if not nombre.isdigit():
		print("Ce n'est pas un nombre")
		continue
	elif nombre<0 or nombre>100: 
		continue
	else:
		if nombre_mystere<nombre:
			print(f"Le nombre mystère est plus petit que {nombre}")
			tour-=1
			continue
		elif nombre_mystere>nombre:
			print(f"Le nombre mystère est plus grand que {nombre}")
			tour-=1
			continue
		else:
			print(f"Félicitation!!! Le nombre mystère est {nombre_mystere}")
			break