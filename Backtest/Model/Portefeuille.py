class Portefeuille:

    def __init__(self,btcVol,eurVol):
        self._currency_ = 'BTC-EUR'
        self._BtcVol_ = btcVol
        self._EurVol_ = eurVol
        self._pendingBtcVol_ = btcVol
        self._pendingEurVol_ = eurVol

