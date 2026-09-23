from tkinter import *
from objet import *
from fonction import *
from tkinter import ttk

##################################### Variables Utiles #####################################

pieces = charger_piece() #L'ensemble de la description des pieces pour chaque etages
piece_actuelle = 1 #Piece dans laquelle se trouve le joueur 
etage_actuel = 1 # Etage dans lequelle se trouve le joueur
label_etage = None
bouton_continuer = None

############################################################################################

root = Tk()
root.title("Castle Explorer")

label_nom = ttk.Label(root, text="Quel est ton nom jeune aventurier ?")
label_nom.pack()

entry_nom = ttk.Entry(root)
entry_nom.pack()

label_resultat = ttk.Label(root, text="")
label_resultat.pack()

def valider():
    global label_etage
    global bouton_continuer
    nom_saisi = entry_nom.get()

    if verifier_nom(nom_saisi):
        joueur = Personnage(100, 0, nom_saisi, 10, 10, "Vivant")

        for widget in root.winfo_children():
            widget.destroy()

        label_etage = ttk.Label(root, text=pieces[etage_actuel, piece_actuelle])
        label_etage.pack()

        bouton_continuer = ttk.Button(root, text="Continuer", command=piece_suivante)
        bouton_continuer.pack()
    else:
        label_resultat.config(text="Nom invalide (lettres uniquement, 10 caractères max), réessaie.")

def piece_suivante():
    global piece_actuelle
    global etage_actuel
    global label_etage
    global bouton_continuer

    piece_actuelle += 1

    if piece_actuelle == 4:
        piece_actuelle = 1
        etage_actuel += 1

    label_etage.config(text=pieces[etage_actuel, piece_actuelle])

    if etage_actuel == 21 and piece_actuelle == 2:
        bouton_continuer.config(state="disabled")


bouton_valider = ttk.Button(root, text="Valider", command=valider)
bouton_valider.pack()

root.mainloop()