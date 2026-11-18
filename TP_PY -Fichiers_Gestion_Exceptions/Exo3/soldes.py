


import csv

soldes = {}
lignes_ignorees = 0

with open("operations.csv", "r", encoding="utf-8") as fichier:

    lecteur = csv.DictReader(fichier, delimiter=";")

    for numero, operation in enumerate(lecteur, start=2):

        compte = operation["compte"]
        type_operation = operation["type"]
        montant_texte = operation["montant"].strip()

        try:
            montant = float(montant_texte)

        except ValueError:
            lignes_ignorees += 1
            print("Ligne ignorée :", numero)
            continue

        # Initialiser le compte
        if compte not in soldes:
            soldes[compte] = 0

        # Calculer le solde
        if type_operation == "Dépôt":
            soldes[compte] += montant

        elif type_operation == "Retrait":
            soldes[compte] -= montant


# Afficher les soldes
print("\nSOLDES DES COMPTES")

for compte, solde in soldes.items():
    print(compte, ":", solde, "MRU")


# Afficher le nombre de lignes ignorées
print("\nNombre de lignes ignorées :", lignes_ignorees)


# Enregistrer les soldes dans soldes.csv
with open("soldes.csv", "w", newline="", encoding="utf-8") as fichier:

    ecrivain = csv.writer(fichier, delimiter=";")

    ecrivain.writerow(["compte", "solde"])

    for compte, solde in soldes.items():
        ecrivain.writerow([compte, solde])

print("Les soldes ont été enregistrés.")
