class Portefeuille:

    def __init__(self,btcVol=0,eurVol=100):
        self._currency = 'BTC-EUR'
        self._BtcVol = btcVol
        self._EurVol = eurVol
        self._pendingBtcVol = btcVol
        self._pendingEurVol = eurVol

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

    def _get_currency(self):
        return self._currency

    currency = property(_get_currency())