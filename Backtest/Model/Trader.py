from .Portefeuille import Portefeuille

class Trader:

    def __init__(self):
        self.portefeuille = Portefeuille()


    def passer_ordre_marché(self):
        return 1

    def passer_ordre_stop(self):
        return 1

    def passer_ordre_limit(self):
        return 1