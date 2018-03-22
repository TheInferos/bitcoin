import requests


def multiaddress(address):
    addresses = []
    req = requests.get("https://test-insight.bitpay.com/api/addr/" + str(address)).json()
    for trans in req["transactions"]:
        transReq = requests.get("https://test-insight.bitpay.com/api/tx/" + str(trans)).json()
        if len(transReq["vin"]) > 1:
            print transReq["vin"]
            for transDetails in transReq["vin"]:
                addresses.append(str(transDetails["addr"]))
    return addresses



#print(multiaddress("2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"))