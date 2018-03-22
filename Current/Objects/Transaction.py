import requests
class Transaction():
    def __init__(self, id):
        self.id = id
        self.req = res = requests.get("https://test-insight.bitpay.com/api/tx/" + str(id)).json()
        self.vIn = res["vin"]
        self.vOut = res["vout"]
        self.Inadds = []
        for i in self.vIn:
            self.Inadds.append(str(i['addr']))
        self.Outadds = []
        for i in self.vOut:
            self.Outadds.append(str(i["scriptPubKey"]["addresses"][0]))
        #self.payee = payee
        #self.recipent = recipient
        # insert pass data
    def getAddresses(self):
        return self.Inadds + self.Outadds
#tx = Transaction("0076a2b49e76585af5785e61a1b97378afd84e9e098c3dce73ff53df9dc8577f")