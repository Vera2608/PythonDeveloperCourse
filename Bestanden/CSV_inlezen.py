# import csv
# from collections import Counter
#
# gender_counts = Counter()
#
# with open('Smartphone_Usage_Productivity_Dataset_50000.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         gender = row['Gender'].strip()  # removes extra spaces
#         gender_counts[gender] += 1
#
# for gender, count in gender_counts.items():
#     print(f"{gender}: {count}")

import csv

# Lijst met namen en cijfers
gegevens = [("Anna", 7.5), ("Rik", 8.2), ("Mila", 6.9)]

bestandsnaam = "cijfers.csv"

# Gegevens opslaan in CSV-bestand
with open(bestandsnaam, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["naam", "cijfer"])  # kolomnamen
    writer.writerows(gegevens)

# CSV-bestand opnieuw openen en gemiddelde berekenen
totaal = 0
aantal = 0

with open(bestandsnaam, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        totaal += float(row["cijfer"])
        aantal += 1

gemiddelde = totaal / aantal if aantal > 0 else 0

# Gemiddelde tonen met f-string
print(f"Het gemiddelde cijfer is: {gemiddelde:.2f}")