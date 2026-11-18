


janvier = ["C01", "C02", "C03", "C05", "C08"]

fevrier = ["C02", "C03", "C04", "C08", "C09"]

mars = ["C01", "C03", "C08", "C09", "C10"]

# 1. Clients venus les trois mois
clients_trois_mois = (
    set(janvier) & set(fevrier) & set(mars)
)

print("Clients des trois mois :", sorted(clients_trois_mois))

# 2. Clients venus au moins une fois
tous_clients = (
    set(janvier) | set(fevrier) | set(mars)
)

print("Tous les clients :", sorted(tous_clients))

# 3. Nouveaux clients de mars
nouveaux = (
    set(mars) - (set(janvier) | set(fevrier))
)

print("Nouveaux clients de mars :", sorted(nouveaux))
