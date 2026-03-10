class Film:
    def __init__(self, titel, score):
        self.titel = titel
        self.score = score
        self.__inkomsten = 0
    def inkomsten(self, bedrag):
        self.__inkomsten += bedrag
    def get_inkomsten(self):
        return self.__inkomsten
    # def __repre__(self):
    #     return f' Film ({self.titel}, {self.score})'
    def __str__(self):
        return f'Film ({self.titel}, {self.score})'