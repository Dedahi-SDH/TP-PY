


produits = []
total = 0

with open("produits.txt", "r", encoding="utf-8") as fichier:

    for ligne in fichier:

        designation, prix = ligne.strip().split(";")

        prix = float(prix)

        produits.append((designation, prix))

        total += prix


# Affichage du tableau
print(f"{'Désignation':<25} {'Prix':>12}")
print("-" * 40)

for designation, prix in produits:

    print(f"{designation:<25} {prix:>12.2f}")


# Calcul de la moyenne
moyenne = total / len(produits)

print("-" * 40)
print(f"Prix moyen : {moyenne:.2f} MRU")
