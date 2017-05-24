class Portefeuille:

    def __init__(self,btcVol=0,eurVol=100):
        self.currency = 'BTC-EUR'
        self.BtcVol = btcVol
        self.EurVol = eurVol
        self.pendingBtcVol = btcVol
        self.pendingEurVol = eurVol

    def change_btc_amount(self,amount,isorder):
        if not isorder:
            self._BtcVol_ += amount
        else:
            self._pendingBtcVol_ += amount

    def change_eur_amount(self,amount,isorder):
        if not isorder:
            self._EurVol_ += amount
        else:
            self._pendingEurVol += amount

