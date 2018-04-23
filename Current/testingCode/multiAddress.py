import os
def lookUpAddress(address):
    fileName = "MultiAddressWatchlist/" + address[0:5]
    if os.path.isfile(fileName):
        f = open(fileName, "r")
        splitF = f.read().split("\n")
        otherAddresses = []
        certainty = []
        found = False
        for lines in splitF:
            line = lines.split(" ")
            if line[0] == address :
                found = True
                values = line[1:len(line)]
                #print (values)
                for vals in values:
                    test = vals.split(":")
                    otherAddresses.append(test[0])
                    certainty.append(test[1])
                return otherAddresses, certainty
    return otherAddresses, certainty

#
# def saveAddress(address1, address2, certainty):
#     lookUpAddress(address1)
#     lookUpAddress(address2)
#     if address1 != []:
#         pass
    
#lookUpAddress("2N672VWCiPhob46jEVrpohd47Xqg7koufug")
