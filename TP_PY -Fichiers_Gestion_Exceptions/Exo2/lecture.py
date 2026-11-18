


import csv
from datetime import datetime

with open("operations.csv", "r", encoding="utf-8") as fichier:

    lecteur = csv.DictReader(fichier, delimiter=";")

    for operation in lecteur:

        # Récupérer les informations
        date = operation["date"]
        compte = operation["compte"]
        type_operation = operation["type"]
        montant = int(operation["montant"])

        # Convertir la date
        date = datetime.strptime(
            date, "%Y-%m-%d"
        ).strftime("%d/%m/%Y")

        # Afficher l'opération
        print(
            date,
            compte,
            type_operation,
            f"{montant:,}".replace(",", " ")
        )
