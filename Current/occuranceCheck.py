import namer
import compareAddresses
from Objects import Address as addr
from Objects import Transaction as Trans

def simpleOccuranceCheck(address1,address2):
    occurance = compareAddresses.simpleCompare( address1, address2)
    names = namer.passNamedAdds()
    address1 = namer.lookupName(address1, names)
    address2 = namer.lookupName(address2, names)
    if occurance != []:
        message = ""
        for i in occurance:
            message += i + ", "
        if len(occurance) == 1:
            amount = " hash "
        else:
            amount = " hashes "
        return("There is an occurance between " + address1 +" and " + address2 + " at trancation " + amount + message), True
    else:
        return "There is no occurance", False

def listOccuranceCheck(list1, list2):
    occurance = compareAddresses.listCompare(list1, list2)
    names = namer.passNamedAdds()
    l1Name= ""
    for item in list1:
        if l1Name == "":
            temp = namer.lookupName(item, names)
            if temp != item:
                l1Name = temp
    l2Name = ""
    for item in list2:
        if l2Name == "":
            temp = namer.lookupName(item, names)
            if temp != item:
                l2Name = temp
    if occurance != []:
        message = ""
        for i in occurance:
            message += i + ", "
        if len(occurance) == 1:
            amount = " hash "
        else:
            amount = " hashes "
        if l1Name != "":
            list1 = l1Name
        if l2Name != "":
            list2 = l2Name
        return("There is an occurance between" , list1 ," and " , list2 , "at trancation " + amount + message), True
    else:
        return "There is no occurance", False

def checkOverLeapsSetup(list1, list2):
    l1Class = convertAddrs(list1)
    l2Class = convertAddrs(list2)
    l1Trans = []
    l1numTrans = 0
    for item in l1Class:
        l1Trans.append(item.tx)
        l1numTrans += len(item.tx)
    l2Trans = []
    l2numTrans = 0
    for item in l2Class:
        l2Trans.append(item.tx)
        l2numTrans += len(item.tx)
    i = 2
    l1Expansion = [l1Class]
    l2Expansion = [l2Class]
    return l1Class,l1numTrans,l1Trans,l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion

def checkOverLeaps(list1,list2, leaps):
    l1Class, l1numTrans, l1Trans, l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion = checkOverLeapsSetup(list1, list2)
    return checkOverLeapsFunction(l1Class, l1numTrans, l2Trans, l1Expansion, l2Class, l2numTrans, l1Trans, l2Expansion, leaps)

def checkOverLeapsFunction(l1Class, l1numTrans, l1Trans, l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion, leaps):
    i = 2
    where, occurance = checkClassOccurances(l1Class,l2Class)
    while (occurance == False) and (i < leaps):
        if occurance == False:
            if l1numTrans <= l2numTrans:
                shorter = l1Trans
                shortList = 1
                other = l2Trans
            else:
                shorter = l2Trans
                shortList = 2
                other = l1Trans
            for item in shorter:
                if item in other:
                    occurance = True
                else:
                    addrs = obsucate1Step(shorter)
                    additions = convertAddrs(addrs)
                    if shortList == 1:
                        for item in additions:
                            for known, addressAt in enumerate(l1Class):
                                if addressAt.hash == item.hash:
                                    del l1Class[known]
                                    break
                        l1Expansion.append(additions)
                        l1Class += additions
                    else:
                        for item in additions:
                            for known, addressAt in enumerate(l2Class):
                                if addressAt.hash == item.hash:
                                    del l2Class[known]
                                    break
                        l2Expansion.append(additions)
                        l2Class += additions
                    occurances, occurance = checkClassOccurances(l1Class,l2Class)

                    return occurance, occurances, l1Expansion, l2Expansion
        i += 1
    occurances = ""
    return occurance, occurances, l1Expansion, l2Expansion

def checkClassOccurances (addressList1, addressList2):
    trans1 = []
    for set1 in addressList1:
        for trans in set1.tx:
            trans1.append(trans)
    trans2 = []
    for set2 in addressList2:
        for trans in set2.tx:
            trans2.append(trans)
    shorter,longer = shorterLongerList(trans1,trans2)
    occurance = []
    for trans in shorter:
        if trans in longer:
            occurance.append(str(trans))
    if occurance != []:
        return occurance, True
    return occurance, False

def shorterLongerList(l1,l2):
    if len(l1) <= len(l2):
        shorter = l1
        longer = l2
    else:
        shorter = l2
        longer = l1
    return shorter, longer

def shorterLonger(l1,l2):
    if l1 <= l2:
        shorter = l1
        longer = l2
    else:
        shorter = l2
        longer = l1
    return shorter, longer

def addrSetupLeaps(list):# pass it transactions
    txList = []
    for item in list:
        txList.append(Trans(item))
    return txList

def convertAddrs(list1):
    addrs = []
    for item in list1:
        addrs.append(addr.Address(item))
    return addrs

def obsucate1Step(transactions):
    addressList = []
    completeList = []
    for item in transactions:
        for trans in item:
            completeList.append(Trans.Transaction(trans).getAddresses())
    for item in completeList:
        for addresses in item:
            addressList.append(addresses)

    return list(set(addressList))

def reverseSteps(occurances, exp1, exp2):
    exp1Route = []
    exp2Route = []
    for i in occurances:
        exp1Len = 0#len(exp1)
        exp2Len = 0#len(exp2)
        exp1Steps = []
        exp2Steps = []
        exp1Solved = False
        exp2Solved = False
        exp1Steps.append(findTransAddCross(i, exp1[-1]))
        exp2Steps.append(findTransAddCross(i, exp2[-1]))
        while not(exp1Solved) and not(exp2Solved):
            if exp1Solved == False:
                pass
            if exp2Solved == False:
                pass
            if exp1Len == 0:
                exp1Solved = True
            if exp2Len == 0:
                exp2Solved = True
            print "got in"

def findTransAddCross(transaction, addresses):
    trans = Trans.Transaction(transaction)
    addrs= trans.getAddresses()
    occuances = []
    for i in addrs:
        for addrHash in addresses:

            if i == addrHash.hash:
                occuances.append([i, transaction])
    return occuances

def findInEarlier(exp, address):
    lowestAdd = -1
    for ident in range(exp):
        if lowestAdd == -1:
            for single in exp[ident]:
                if address == single.hash:
                    lowestAdd = ident
    return 


def demoSingle():
    address1 = "mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei" #input("Please enter the first address ")
    address2 = "mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W" #input("Please enter the second address ")
    return simpleOccuranceCheck(address1, address2)


def demoList():
    list1 = ["mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei"] #input("Please enter the first address ")
    list2 = ["mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W"]#input("Please enter the second address ")
    return listOccuranceCheck(list1, list2)

def demoCheckOverLeaps():
    list1 = ["mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei"]
    list2 = ["moUkGQDCFqfbpbkETscTcX2fouLN8tnfQY"]
    occurance, occurances, l1Expansion, l2Expansion = checkOverLeaps(list1,list2,3)
    reverseSteps(occurances,l1Expansion,l2Expansion)


print(demoSingle())
#print (demoList())
#occurance, occurances, l1Expansion, l2Expansion = demoCheckOverLeaps()
#print l1Expansion
#print demoCheckOverLeaps()