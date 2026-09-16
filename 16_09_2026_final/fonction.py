def verifier_nom(nom):
    if nom.isalpha() and len(nom) <= 10:
        return True
    else:
        return False

nom = "Apzozjdudo"
verifier_nom(nom)
print(verifier_nom(nom))