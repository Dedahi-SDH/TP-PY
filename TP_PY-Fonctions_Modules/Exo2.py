def valeur_acquise(capital, taux, annees):
    return capital*(1 + taux/100)**annees


def mensualite(capital, taux_annuel, mois):
    taux_mensuel = taux_annuel / 100 / 12

    if taux_mensuel == 0:
        return capital / mois

    m = (capital * taux_mensuel) / (1 - (1 + taux_mensuel) ** (-mois))

    return m

def cout_credit(capital, taux_annuel, mois):
    m = mensualite(capital, taux_annuel, mois)
    total_paye = m * mois
    return total_paye - capital


capital = 500000
taux_annuel = 12

for mois in [12, 24, 36]:

    m = mensualite(capital, taux_annuel, mois)
    cout = cout_credit(capital, taux_annuel, mois)

    print("Durée :", mois, "mois")
    print("Mensualité :", round(m, 2), "MRU")
    print("Coût du crédit :", round(cout, 2), "MRU")
    print("-------------------------")