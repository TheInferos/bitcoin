import requests


def multiaddress(address):
    addresses = []
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
    return list(set(addresses))

def moduleTest():
    print "MultiAddress test address: 'n4XL8xce6hQfUyJDhnksfKPn4JKqU4qNTo'"
    print "Expected output:'n4XL8xce6hQfUyJDhnksfKPn4JKqU4qNTo', 'mtUY6inTJbnWxvr2Kwi1AMHbA8fKjNFRST' date April 18 "
    print multiaddress("n4XL8xce6hQfUyJDhnksfKPn4JKqU4qNTo")

#moduleTest()
#print(multiaddress("2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"))
 # multiple multi inputs only one input wanted