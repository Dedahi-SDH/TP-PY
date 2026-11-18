
import gestion_stock

# Déclaration des données
stock = {
    "P01": 4,
    "P02": 15,
    "P03": 8,
    "P04": 120
}

prix = {
    "P01": 45000,
    "P02": 12000,
    "P03": 6500,
    "P04": 350
}

# 1. Calculer la valeur du stock
valeur = gestion_stock.valeur_stock(stock, prix)

print("Valeur totale du stock :", valeur, "MRU")

# 2. Rechercher les produits en rupture
liste_ruptures = gestion_stock.ruptures(stock)

print("Produits en rupture :", liste_ruptures)

# 3. Réapprovisionner P01
nouvelle_quantite = gestion_stock.reapprovisionner(
    stock, "P01", 10
)

print("Nouvelle quantité de P01 :", nouvelle_quantite)

# Afficher le stock après réapprovisionnement
print("Stock actualisé :", stock)
