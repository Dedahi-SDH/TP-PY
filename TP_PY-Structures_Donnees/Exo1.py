
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

ventes = [125000, 98000, 143500, 87000, 210000, 176500]

# a) Total et moyenne
total = sum(ventes)
moyenne = total / len(ventes)

print("Total :", total)
print("Moyenne :", moyenne)

# b) Jour avec la vente maximale
vente_max = max(ventes)
position = ventes.index(vente_max)

print("Meilleur jour :", jours[position])
print("Vente maximale :", vente_max)

# c) Jours dont les ventes dépassent la moyenne
print("\nJours au-dessus de la moyenne :")

for i in range(len(ventes)):
    if ventes[i] > moyenne:
        print(jours[i], ":", ventes[i])

# d) Classement décroissant
print("\nClassement des ventes :")

classement = sorted(zip(ventes, jours), reverse=True)

for vente, jour in classement:
    print(jour, ":", vente)
