import requests


def ShadowAddressCluster(address):
    addresses = []
    req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(address)).json() # get address details
    for xtion in req["transactions"]: # loop through transaction list
        transReq = requests.get("https://test-insight.bitpay.com/api/tx/" + str(xtion)).json() # get the transaction details
        if transReq["vout"] > 1: # if there is more than one output
            tempAd = "" # check before
            firstInstances = 0 #
            for i in (transReq["vout"]): # loop through the o   utputs
                if "addresses" in i["scriptPubKey"]:
                    addr = i["scriptPubKey"]["addresses"][0] # get the output address
                    print addr
                    tempreq = requests.get("https://test-insight.bitpay.com/api/addr/" + str(addr)).json() # get the new addresses tranaction list
                    if "transactions" in tempreq:
                        print tempreq["transactions"]
                        if str(tempreq["transactions"][-1]) == str(xtion): # if this was the first transaction it was involved in
                            tempAd += str(addr)
                            firstInstances += 1
            if firstInstances == 1:
                addresses.append(tempAd)
    cluster = []
    for addr in addresses:
        req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(addr)).json()
        trans = req["transactions"]
        trans = trans [-1]
        req = requests.get("https://test-insight.bitpay.com/api/tx/" + str(trans)).json() # get the transaction details
        for i in req["vin"]:
            cluster.append(str(i["addr"]))
        cluster.append(addr)
    return (cluster)


def addAddresses(addresses, code):
    for addr1 in addresses:
        message = str(addr1) + " "
        for addr2 in addresses:
            if addr1 != addr2:
                 message += addr2 + " " + code + " "
    return message


#print(ShadowAddressCluster("moydwVNxX2tsb2Q3aPvWLnAPgZ7t3dNQSe"))
#2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN and 2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF

