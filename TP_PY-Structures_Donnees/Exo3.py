


catalogue = {
    "P01": {"nom": "Ordinateur portable", "categorie": "Informatique", "prix": 45000},
    "P02": {"nom": "Imprimante", "categorie": "Informatique", "prix": 12000},
    "P03": {"nom": "Chaise de bureau", "categorie": "Mobilier", "prix": 6500},
    "P04": {"nom": "Ramette papier", "categorie": "Fournitures", "prix": 350}
}

# a) Ajouter P05
catalogue["P05"] = {
    "nom": "Bureau",
    "categorie": "Mobilier",
    "prix": 18000
}

# b) Augmenter les prix Informatique de 5 %
for ref, produit in catalogue.items():
    if produit["categorie"] == "Informatique":
        produit["prix"] = round(produit["prix"] * 1.05)

# c) Supprimer P04
del catalogue["P04"]

# d) Afficher le catalogue
print("CATALOGUE DES PRODUITS")
print(f"{'Référence':<12} {'Nom':<25} {'Catégorie':<18} {'Prix':>10}")

for ref, produit in catalogue.items():
    print(
        f"{ref:<12} "
        f"{produit['nom']:<25} "
        f"{produit['categorie']:<18} "
        f"{produit['prix']:>10}"
    )

# e) Prix moyen par catégorie
categories = {}

for produit in catalogue.values():
    categorie = produit["categorie"]
    prix = produit["prix"]

    if categorie not in categories:
        categories[categorie] = []

    categories[categorie].append(prix)

print("\nPRIX MOYEN PAR CATEGORIE")

for categorie, prix_liste in categories.items():
    moyenne = sum(prix_liste) / len(prix_liste)
    print(categorie, ":", moyenne, "MRU")
