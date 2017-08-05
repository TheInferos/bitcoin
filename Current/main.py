from bitcoin.Current import namer
from bitcoin.Current import compareAddresses

address1 = "n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7"
address2 = "2N672VWCiPhob46jEVrpohd47Xqg7koufug"
occurance = compareAddresses.simpleCompare( address1, address2)
names = namer.passNamedAdds()
address1 = namer.lookupName(address1, names)
address2 = namer.lookupName(address2, names)
if occurance != []:
    message = ""
    for i in occurance:
        message += i + " "
    if len(occurance) == 1:
        amount = " transaction hash "
    else:
        amount = " transaction hashes "
    print("There is an occurance between " + address1 +" and " + address2 + " at trancation " + amount + message)