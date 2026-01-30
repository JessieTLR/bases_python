import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower = phrase.lower()

alphabet=string.ascii_lowercase

comparaison=set(phrase_lower)<= set(alphabet)




print(comparaison)

