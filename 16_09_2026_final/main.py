from tkinter import *
from objet import *
from fonction import *
from tkinter import ttk

root = Tk()
root.title("Castle Explorer")

label_nom = ttk.Label(root, text="Quel est ton nom jeune aventurier ?")
label_nom.pack()

entry_nom = ttk.Entry(root)
entry_nom.pack()

label_resultat = ttk.Label(root, text="")
label_resultat.pack()

def valider():
    nom_saisi = entry_nom.get()
    if verifier_nom(nom_saisi):
        joueur = Personnage(100, 0, nom_saisi, 10, 10, "Vivant")
        label_resultat.config(text=f"Bienvenue au chateau {joueur.nom} !")
    else:
        label_resultat.config(text="Nom invalide (lettres uniquement, 10 caractères max), réessaie.")

bouton_valider = ttk.Button(root, text="Valider", command=valider)
bouton_valider.pack()

root.mainloop()