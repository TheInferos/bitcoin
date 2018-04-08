import requests


def multiaddress(address):
    addresses = []
    i = 0
    req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(address)).json()
    for trans in req["transactions"]:
        transReq = requests.get("https://test-insight.bitpay.com/api/tx/" + str(trans)).json()
        if len(transReq["vin"]) > 1:
            addsIn = []
            for transDetails in transReq["vin"]:
                addsIn.append(str(transDetails["addr"]))
            if address in addsIn:
                for add in addsIn:
                    addresses.append(add)
        i += 1
        print i
    return list(set(addresses))



#print(multiaddress("2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"))
print multiaddress("n4XL8xce6hQfUyJDhnksfKPn4JKqU4qNTo") # multiple multi inputs only one input wanted