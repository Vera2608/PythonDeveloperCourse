from persoon import Persoon

class Docent(Persoon):
    def __init__(self, naam, leeftijd, vak):
        super().__init__(naam, leeftijd) #je neemt de naam en leeftijd over uit de parent/super class
        self.vak = vak
    # def __repr__(self):
    #     return f"Docent({self.naam}, {self.leeftijd}, {self.vak})"
#     de repr wordt gebruikt voor debuggen, voor output/gebruiker gebruik is eerder __str__, dan wordt de classe niet opnieuw benoemd.
    def __str__(self):
        return f'{self.naam} {self.leeftijd} {self.vak}'

