class Personnage :

    def __init__(self, pv, argent, nom, attaque, defense, etat):
        self.pv = pv 
        self.argent = argent
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.etat = etat

    def perd_de_la_vie(self, degat): #Verifie si le personnage perd de la vie
        pv = self.pv - degat
        self.pv = pv

    def attaquer(self, Personnage): #Permet a un personnage d'en attaquer un autre et retourne le résultat 
        degat = self.attaque - Personnage.defense
        if(degat <= 0):
            return f"L'attaque du combattant {self.nom} n'est pas éfficace"
        else:
            pv_final = Personnage.pv - degat
            Personnage.pv = pv_final
            return f"Le combattant {Personnage.nom} perd {degat} pv"

class Ennemi(Personnage) : #Personnage ennemi, possede un butin et de l'or
    def __init__(self, pv, argent, nom, attaque, defense, etat, or_butin, objet_butin):
        super().__init__(pv, argent, nom, attaque, defense, etat)
        self.or_butin = or_butin
        self.objet_butin = objet_butin

class PNJ(Personnage) : #Personnage neutre (marchand, explorateur, villageois etc...) possede or ou objet pour le joueur 
    def __init__(self, pv, argent, nom, attaque, defense, etat, or_transaction, objet_transaction):
        super().__init__(pv, argent, nom, attaque, defense, etat)
        self.or_transaction = or_transaction
        self.objet_transaction = objet_transaction

###### Tests #######

Marchand = PNJ(1,0,"Keke",1,1,"Vivant",100,"Rien")
Gobelin = Ennemi(100,0,"Keko",5,2,"Vivant",2,"Rien")
Toto = Personnage(100,0,"Toto",60,10,"Vivant")
