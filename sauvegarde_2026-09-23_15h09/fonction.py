import csv

def verifier_nom(nom): # Au lancement du jeu on verifie si le nom est conforme.
    if nom.isalpha() and len(nom) <= 10:
        return True
    else:
        return False

def charger_piece(): # On charge le dictionnaire en entier, pour afficher les descriptions au fur et a mesure
    pieces = {}
    with open("ressources/pieces.csv", newline="", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            etage = int(ligne["etage"])
            piece = int(ligne["piece"])
            texte = str(ligne["texte"])
            pieces[etage, piece] = texte
    return pieces

