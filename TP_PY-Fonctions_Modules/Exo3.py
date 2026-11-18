
def facturer(lignes, catalogue, remise=0.0):

    brut = 0

    for reference, quantite in lignes:

        if reference not in catalogue:
            raise KeyError("Référence inconnue")

        prix = catalogue[reference]
        brut = brut + (prix * quantite)

    montant_remise = brut * remise
    net_ht = brut - montant_remise
    tva = net_ht * 0.16
    ttc = net_ht + tva

    return {
        "brut": brut,
        "remise": montant_remise,
        "net_ht": net_ht,
        "tva": tva,
        "ttc": ttc
    }


# Programme principal

catalogue = {
    "P01": 45000,
    "P02": 12000,
    "P03": 6500
}

commande = [
    ("P01", 2),
    ("P03", 4)
]

resultat = facturer(commande, catalogue, 0.05)

print("Montant brut :", resultat["brut"], "MRU")
print("Remise :", resultat["remise"], "MRU")
print("Net HT :", resultat["net_ht"], "MRU")
print("TVA :", resultat["tva"], "MRU")
print("TTC :", resultat["ttc"], "MRU")
