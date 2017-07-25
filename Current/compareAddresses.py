from bitcoin.Current.Objects import Address as addr
import requests

addr1 = addr.Address("n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7")
#addr2 = addr.Address("2N672VWCiPhob46jEVrpohd47Xqg7koufug")
addr2 = "2N672VWCiPhob46jEVrpohd47Xqg7koufug"
match = False


res = requests.get("https://test-insight.bitpay.com/api/tx/" + str(addr1.tx[0])).json()
#print(res["vin"])

occurance = []
for transx in addr1.tx:
    res = requests.get("https://test-insight.bitpay.com/api/tx/" + str(transx)).json()
    for i in res["vin"]:
        if "addr" in res["vin"]:
            if i["addr"] == addr2:
                match = True
                occurance.append(addr1.tx)
    for key in res["vout"]:
         for hash in (key["scriptPubKey"]["addresses"]):
             if hash == addr2:
                match = True
                occurance.append(addr1.tx)

print (occurance)