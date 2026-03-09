# class Auto:
#     def __init__(self, merk, model):
#         self.merk = merk
#         self.model = model
#         self.snelheid = 0
#     def versnellen (self, delta):
#         self.snelheid += delta
#     def remmen (self, alpha):
#         if self.snelheid - alpha < 0:
#              self.snelheid = 0
#         else:
#              self.snelheid -= alpha
#
# a = Auto("Toyota", "Yaris")
# b = Auto("Volvo", "ID4")
# # a.versnellen(80)
# # b.versnellen(50)
#
# autos = [a, b]
# for auto in autos:
#     if auto.merk == "Volvo":
#         auto.versnellen(100)
#     elif auto.merk == "Toyota":
#         auto.remmen(100)
#
#     print(auto.merk, auto.snelheid)


# print("auto", a.merk, "heeft snelheid", a.snelheid)
# print("auto", b.merk, "heeft snelheid", b.snelheid)


from film_class import Film
# films = [Film("Titanic", 8.0), Film ("365 Days", 2.2), Film("Rocky", 8.1), Film("Frankenstein", 7.4)] maar je kan het ook in een losse csv zetten:
import csv
films = []

with open("film_overview.csv", newline="") as f:
    reader = csv.reader(f)
    for rij in reader:
        film = Film(rij[0], float(rij[1]))
        film.inkomsten(10)
        films.append(film)


leukste_films = [s for s in films if s.score >=7.5]
gesorteerd = sorted(leukste_films, key=lambda s: s.score, reverse=True) #normaal van klein naar groot, maar met reverse zetten we het van groot naar klein

for film in films:
    print (f'De volgende film is beschikbaar: ', film)
for film in gesorteerd:
    print(f'Goed beoordeelde film: ', film.titel, film.score, film.get_inkomsten())




#
#
#
# for film in gesorteerd:
#     if film.score >= 7.5:
#         print(film.titel, film.score)
