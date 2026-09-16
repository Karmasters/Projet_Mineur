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

class Ennemi(Personnage) : #Personnage ennemi
    def __init__(self, pv, argent, nom, attaque, defense, etat, or_butin, objet_butin):
        super().__init__(pv, argent, nom, attaque, defense, etat)
        self.or_butin = or_butin
        self.objet_butin = objet_butin

class PNJ(Personnage) : #Personnage neutre 
    def __init__(self, pv, argent, nom, attaque, defense, etat, or_transaction, objet_transaction):
        super().__init__(pv, argent, nom, attaque, defense, etat)
        self.or_transaction = or_transaction
        self.objet_transaction = objet_transaction
        

Marchand = PNJ(1,0,"Keke",1,1,"Vivant",100,"Rien")
Gobelin = Ennemi(1,0,"Keko",1,2,"Vivant",2,"Rien")

print(Marchand.pv)
print(Marchand.argent)
print(Marchand.etat)
print(Gobelin.pv)
print(Gobelin.argent)
print(Gobelin.etat)