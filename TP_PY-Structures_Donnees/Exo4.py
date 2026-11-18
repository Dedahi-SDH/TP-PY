


ventes = [
    ("Aicha", 12000),
    ("Sidi", 8000),
    ("Aicha", 15500),
    ("Mohamed", 4000),
    ("Sidi", 22000),
    ("Aicha", 3000),
    ("Fatimetou", 18000)
]

# a) Nombre de vendeurs distincts
vendeurs = set()

for nom, montant in ventes:
    vendeurs.add(nom)

print("Nombre de vendeurs :", len(vendeurs))

# b) Nombre de ventes par vendeur
nombre_ventes = {}

for nom, montant in ventes:
    if nom not in nombre_ventes:
        nombre_ventes[nom] = 0

    nombre_ventes[nom] += 1

print("Nombre de ventes :", nombre_ventes)

# Chiffre d'affaires par vendeur
chiffre_affaires = {}

for nom, montant in ventes:
    if nom not in chiffre_affaires:
        chiffre_affaires[nom] = 0

    chiffre_affaires[nom] += montant

print("Chiffre d'affaires :", chiffre_affaires)

# c) Classement décroissant
classement = sorted(
    chiffre_affaires.items(),
    key=lambda element: element[1],
    reverse=True
)

print("\nClassement des vendeurs :")

for nom, montant in classement:
    print(nom, ":", montant, "MRU")
