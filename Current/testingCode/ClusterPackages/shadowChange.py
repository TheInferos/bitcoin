import requests


def ShadowAddressCluster(address):
    addresses = []
    req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(address)).json() # get address details
    for xtion in req["transactions"]: # loop through transaction list
        transReq = requests.get("https://test-insight.bitpay.com/api/tx/" + str(xtion)).json() # get the transaction details
        if transReq["vout"] > 1: # if there is more than one output
            tempAd = "" # check before
            firstInstances = 0 #
            for i in (transReq["vout"]): # loop through the outputs
                addr = i["scriptPubKey"]["addresses"][0] # get the output address
                tempreq = requests.get("https://test-insight.bitpay.com/api/addr/" + str(addr)).json() # get the new addresses tranaction list
                if str(tempreq["transactions"][-1]) == str(xtion): # if this was the first transaction it was involved in
                    tempAd += str(addr)
                    firstInstances += 1
            if firstInstances == 1:
                addresses.append(tempAd)
    print addresses


def multiaddress(address):
    addresses = []
    req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(address)).json()
    for trans in req["transactions"]:
        transReq = requests.get("https://test-insight.bitpay.com/api/tx/" + str(trans)).json()
        if len(transReq["vin"]) > 1:
            for transDetails in transReq["vin"]:
                addresses.append(transDetails["addr"])
    print addresses


def addAddresses(addresses, code):
    for addr1 in addresses:
        message = str(addr1) + " "
        for addr2 in addresses:
            if addr1 != addr2:
                 message += addr2 + " " + code + " "
    return message














#multiaddress("2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN")
ShadowAddressCluster("moydwVNxX2tsb2Q3aPvWLnAPgZ7t3dNQSe")
#2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN and  2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF