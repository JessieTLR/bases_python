class Voiture: 
    voiture_crees=0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees+=1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls):
        return cls(marque="lamborgihni", vitesse=250, prix=200000)
    
    @classmethod
    def porsche(cls):
        return cls(marque="porsche", vitesse=220, prix=180000)
    
    @staticmethod
    def afficher_nombre_voiture():
        print(f'vous avez {Voiture.voiture_crees} voitures dans votre garage')

lambo=Voiture.lamborghini()
porsche=Voiture.porsche()
Voiture.afficher_nombre_voiture()