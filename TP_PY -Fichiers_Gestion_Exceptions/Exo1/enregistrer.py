
with open("produits.txt", "w", encoding="utf-8") as fichier:

    for i in range(5):

        designation = input("Donner la désignation du produit : ")

        prix = float(input("Donner le prix du produit : "))

        fichier.write(f"{designation};{prix}\n")

print("Les cinq produits ont été enregistrés.")
