from bitcoin.Current.Objects import Address as addr
import requests
def simpleCompare(addr1Hash, addr2Hash):
    addr1 = addr.Address(addr1Hash)
    addr2 = addr.Address(addr2Hash)
    if len(addr1.tx) <= len(addr2.tx):
        shorter = addr1
        compAddr = addr2.hash
    else:
        shorter = addr2
        compAddr = addr1.hash
    occurance = []
    for transx in shorter.tx:
        res = requests.get("https://test-insight.bitpay.com/api/tx/" + str(transx)).json()
        for i in res["vin"]:
            if "addr" in res["vin"]:
                if i["addr"] == compAddr:
                    occurance.append(transx)
        for key in res["vout"]:
             for hash in (key["scriptPubKey"]["addresses"]):
                 if hash == compAddr:
                    occurance.append(transx)
    return occurance
print(simpleCompare("n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7", "2N672VWCiPhob46jEVrpohd47Xqg7koufug"))