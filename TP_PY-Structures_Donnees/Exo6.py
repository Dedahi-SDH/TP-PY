


montants = [1200, -350, 4800, 0, 15000, -90, 700]

# a) Montants strictement positifs
positifs = [m for m in montants if m > 0]

print("Montants positifs :", positifs)

# b) Valeurs absolues
valeurs_absolues = [abs(m) for m in montants]

print("Valeurs absolues :", valeurs_absolues)

# c) Montants positifs avec TVA de 16 %
montants_ttc = [
    round(m * 1.16) for m in montants if m > 0
]

print("Montants TTC :", montants_ttc)
