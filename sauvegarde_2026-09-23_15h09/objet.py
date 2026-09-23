class Personnage :

    def __init__(self, pv, argent, nom, attaque, defense, etat, arme=None, armure=None, inventaire=None):
        self.pv = pv 
        self.argent = argent
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.etat = etat
        self.arme = arme
        self.armure = armure

        if inventaire is None:
            self.inventaire = []
        else:
            self.inventaire = inventaire

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

    def ramasser_objet(self, Objet): #Le personnage ramasse l'objet 
        self.inventaire.append(Objet)

    def equiper_objet(self, Objet): #Le personnage equipe l'objet
        type_cible = Objet.type_objet

        if type_cible == "armure":
            if self.armure != None:
                self.deequiper_objet(self.armure)
                self.armure = Objet
                self.defense += Objet.valeur_stat
            else:
                self.armure = Objet
                self.defense += Objet.valeur_stat

        elif type_cible == "arme":
            if self.arme != None:
                self.deequiper_objet(self.arme)
                self.arme = Objet
                self.attaque += Objet.valeur_stat
            
            else:
                self.arme = Objet
                self.attaque += Objet.valeur_stat

        else :
            return "c'est cassé"

    def deequiper_objet(self, Objet):
        type_cible = Objet.type_objet
        if type_cible == "arme":
            self.attaque -= Objet.valeur_stat
            self.arme = None
        elif type_cible == "armure":
            self.defense -= Objet.valeur_stat
            self.armure = None
        else:
            return "c'est cassé"


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

class Objet(): # Un objet peut être équipé par un joueur ou stocké dans son inventaire. Il peut être vendu. Il donnera selon son type des valeurs de défense ou d'attaque.
    def __init__(self, nom, type_objet, valeur_stat, valeur_or):
        self.nom = nom
        self.type_objet = type_objet
        self.valeur_stat = valeur_stat
        self.valeur_or = valeur_or

###### Tests #######

Marchand = PNJ(1,0,"Keke",1,1,"Vivant",100,"Rien")
Gobelin = Ennemi(100,0,"Keko",5,2,"Vivant",2,"Rien")
Toto = Personnage(100,0,"Toto",60,10,"Vivant")
