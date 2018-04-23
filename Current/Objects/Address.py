import requests


class Address:
    def __init__(self, hash):
        self.hash = str(hash)
        res = requests.get("https://test-insight.bitpay.com/api/addr/" + str(hash)).json()
        self.tx = res["transactions"]
        self.leapCent = [] # used in check over leaps for Transactions
        self.leapBeg = [] # used in check over leaps for Transactions
        self.NextAddress =[] # used in check over leaps for Addresses
        self.PreviousAddress =[] # used in check over leaps for Addresses

#[<Objects.Address.Address instance at 0x04D14DF0>, u'd47dad15486056607c1ffd5723dc24c8663891c991ac04e30704e82bae9cc0fb', <Objects.Address.Address instance at 0x04EE1170>]
#[<Objects.Address.Address instance at 0x04D14DF0>, u'd47dad15486056607c1ffd5723dc24c8663891c991ac04e30704e82bae9cc0fb', <Objects.Address.Address instance at 0x04EE1170>]