from .Portefeuille import Portefeuille

class Trader:

    def __init__(self):
        self.portefeuille = Portefeuille()


    def passer_ordre_marché(self,quantite,prix,sens):
        #need to check if enough funds
        if sens:
            price = -prix
            btcvol = quantite
        else:
            price= prix
            btcvol = -quantite
        self.portefeuille.change_btc_amount(btcvol,True)
        self.portefeuille.change_eur_amount(price,True)

    def passer_ordre_stop(self,quantité,prix,sens):
        return 1

    def passer_ordre_limit(self,quantité,prix,sens):
        return 1