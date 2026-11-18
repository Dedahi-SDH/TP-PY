
# Constante
SEUIL_ALERTE = 10


# Fonction 1 : calculer la valeur totale du stock
def valeur_stock(stock, prix):

    total = 0

    for ref, quantite in stock.items():
        total = total + quantite * prix[ref]

    return total


# Fonction 2 : trouver les produits en rupture
def ruptures(stock, seuil=SEUIL_ALERTE):

    resultat = []

    for ref, quantite in stock.items():

        if quantite < seuil:
            resultat.append(ref)

    return sorted(resultat)


# Fonction 3 : réapprovisionner un produit
def reapprovisionner(stock, ref, quantite):

    if ref not in stock:
        stock[ref] = 0

    stock[ref] = stock[ref] + quantite

    return stock[ref]
