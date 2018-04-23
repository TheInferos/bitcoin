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
        return str("There is an occurance between " + address1 +" and " + address2 + " at trancation " + amount + message), True
    else:
        return "There is no occurance between " + address1 + " and " + address2, False

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
        if l1Name != "":
            list1 = l1Name
        if l2Name != "":
            list2 = l2Name
        return "There is no occurance between ", list1, " and ", list2, False

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
    l1Expansion =[[]]
    for item in l1Class:
        l1Expansion[0].append(item)
    l2Expansion = [[]]
    for item in l2Class:
        l2Expansion[0].append(item)
    return l1Class,l1numTrans,l1Trans,l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion

def checkOverLeaps(list1,list2, leaps):
    l1Class, l1numTrans, l1Trans, l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion = checkOverLeapsSetup(list1, list2)
    occurance, occurances, l1Expansion, l2Expansion = checkOverLeapsFunction(l1Class, l1numTrans, l1Trans, l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion, leaps)
    if occurance == True:
        print "Reversing steps"
        exp1Route, exp2Route = reverseSteps(occurances, l1Expansion, l2Expansion)
        occurance=  writeMessageOverLeaps(exp1Route,exp2Route, occurances)
    else:
        print "There is no connection between ", list1, " and ", list2, " within ", leaps, " steps."
    return occurance

def checkOverLeapsFunction(l1Class, l1numTrans, l1Trans, l1Expansion, l2Class, l2numTrans, l2Trans, l2Expansion, leaps):
    stepsTaken = 1 # may change
    occurance = False
    seen1C = []
    seen1T = []
    seen2C = []
    seen2T = []
    while (occurance == False) and (stepsTaken <=leaps):
        occurances, occurance = checkClassOccurances(l1Class, l2Class) # checks to see if there is an occurance
        if occurance == False:
            if l1numTrans <= l2numTrans:
                shorter = l1Trans[-1]
                shortList = 1
                other = l2Trans

            else:
                shorter = l2Trans[-1]
                other = l1Trans
                shortList = 2
            newAddresses, newTransactions = obsucate1Step(shorter)
            additionsC = []
            additionsT = []
            if shortList == 1:
                #Working out which are new addresses
                for item in newAddresses:
                    for ident in l1Class:
                        if item.hash == ident.hash:
                            seen1C.append(item.hash)
                    if item.hash in seen1C:
                        pass
                    else:
                        additionsC.append(item)
                        seen2C.append(item.hash)
                # Saving the new additions
                if additionsC != []:
                    l1Expansion.append([])
                    for address in additionsC:
                        l1Class.append(address)
                        l1Expansion[-1].append(address)
                # Working out which are new transactions
                for item in newTransactions:
                    for ident in l1Trans[-1]:
                        if item == ident:
                            seen1T.append(item)
                    if item in seen1T:
                        pass
                    else:
                        additionsT.append(item)
                        seen1T.append(item)
                # Saving new Transactions
                l1numTrans = len(additionsT)
                l1Trans.append([])
                for item in additionsT:
                    l1Trans[-1].append(item)
            else:
                # Working out the new addresses
                for item in newAddresses:
                    for ident in l2Class:
                        if item.hash == ident.hash:
                            seen2C.append(item.hash)
                    if item.hash in seen2C:
                        pass
                    else:
                        additionsC.append(item)
                        seen2C.append(item.hash)
                # Saving the new additions
                if additionsC != []:
                    l2Expansion.append([])
                    for address in additionsC:
                        l2Class.append(address)
                        l2Expansion[-1].append(address)
                # Working out which are new transactions
                for item in newTransactions:
                    for ident in l2Trans[-1]:
                        if item == ident:
                            seen2T.append(item)
                    if item in seen2T:
                        pass
                    else:
                        additionsT.append(item)
                        seen2T.append(item)
                # Saving new Transactions
                l2numTrans = len(additionsT)
                l2Trans.append([])
                for item in additionsT:
                    l2Trans[-1].append(item)


            stepsTaken += 1
            print "increasing Steps to ", stepsTaken
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
    for trans in transactions:
        completeList.append(Trans.Transaction(trans).getAddresses())
    for item in completeList:
        for addresses in item:
            addressList.append(addresses)
    addressList = list(set(addressList))
    addressClasses = []
    transactions = []
    for address in addressList:
        temp = addr.Address(address)
        addressClasses.append(temp)
        for item in temp.tx:
            transactions.append(item)
    transactions = list(set(transactions))
    return  addressClasses, transactions

def reverseSteps(occurances, exp1, exp2):
    exp1Ident = 1
    exp2Ident = 1
    temp1 = []
    seenT1 = []
    temp2 = []
    seenT2 = []
    lenExp1= len(exp1)
    lenExp2 = len(exp2)
    exp1Route = []
    exp2Route = []
    for i in range(lenExp1):
        exp1Route.append([])
    for i in range(lenExp2):
        exp2Route.append([])
    for item in occurances:
        trans = Trans.Transaction(item)
        conAddresses = trans.getAddresses()
        for address in exp1[-1]:
            if address.hash in conAddresses:
                address.leapCent.append(trans.id)
                if address.hash in seenT1:
                    pass
                else:
                    temp1.append(address)
                    seenT1.append(address.hash)
        for address in exp2[-1]:
            if address.hash in conAddresses:
                address.leapCent.append(trans.id)
                if address.hash in seenT2:
                    pass
                else:
                    temp2.append(address)
                    seenT2.append(address.hash)
    for address in temp1:
        exp1Route[-1].append(address)
    for address in temp2:
        exp2Route[-1].append(address)
    oldTemp1 = []
    oldTemp2 = []
    while (exp1Ident < lenExp1) or (exp2Ident < lenExp2):
        if exp1Ident < lenExp1:
            exp1Ident += 1
            oldTemp1 = temp1
            temp1 = []
            for ident in oldTemp1:
                tempTrans = ident.tx
                for trans in tempTrans:
                    for address in exp1[-exp1Ident]:
                        if trans in address.tx:
                            address.leapCent.append(trans)
                            ident.leapBeg.append(trans)
                            indicator = 0
                            for nextAdd in address.NextAddress:
                                if ident.hash == nextAdd.hash:
                                    indicator = 1
                            if indicator == 0:
                                address.NextAddress.append(ident)
                            indicator = 0
                            for prevAdd in ident.PreviousAddress:
                                if address.hash == prevAdd.hash:
                                    indicator = 1
                            if indicator == 0:
                                ident.PreviousAddress.append(address)
                            if address.hash in seenT1:
                                pass
                            else:
                                temp1.append(address)
                                seenT1.append(address.hash)
            for address in temp1:
                exp1Route[-exp1Ident].append(address)
        if exp2Ident < lenExp2:
            exp2Ident += 1
            oldTemp2 = temp2
            temp2 = []
            for ident in oldTemp2:
                tempTrans = ident.tx
                for trans in tempTrans:
                    for address in exp2[-exp2Ident]:
                        if trans in address.tx:
                            address.leapCent.append(trans)
                            ident.leapBeg.append(trans)

                            address.NextAddress.append(ident)
                            ident.PreviousAddress.append(address)
                            if address.hash in seenT2:
                                pass
                            else:
                                temp2.append(address)
                                seenT2.append(address.hash)
            for address in temp2:
                exp2Route[-exp2Ident].append(address)

    return exp1Route, exp2Route


# def findTransAddCross(transaction, addresses):
#     trans = Trans.Transaction(transaction)
#     addrs= trans.getAddresses()
#     occuances = []
#     for i in addrs:
#         for addrHash in addresses:
#
#             if i == addrHash.hash:
#                 occuances.append([i, transaction])
#     return occuances

def writeMessageOverLeaps(exp1Route, exp2Route, occurances):
    message =""
    stagesR1 =[]
    stagesR2 =[]
    lenR1 = len(exp1Route)
    lenR2 = len(exp2Route)
    r1Ident = 0
    r2Ident = 0
    names = namer.passNamedAdds()
    while r1Ident +1 <lenR1 or r2Ident +1 < lenR2:
        if r1Ident <lenR1:
            stagesR1.append([])
            for item in exp1Route[r1Ident]:
                conAddress = item.NextAddress
                for address in conAddress:
                    for tx in item.leapCent:
                        if tx in address.leapBeg:
                            stagesR1[-1].append([item, str(tx), address])
            r1Ident += 1
        if r2Ident +1 <lenR2:
            stagesR2.append([])
            for item in exp2Route[r1Ident]:
                conAddress = item.NextAddress
                for address in conAddress:
                    for tx in item.leapCent:
                        if tx in address.leapBeg:
                            stagesR2[-1].append([item, tx, address])
            r2Ident += 1
    #insert propoer bits and pecies to form the list nicely
    stagesR1.append([])
    stagesR2.append([])
    finalAdds1 = exp1Route[-1]
    finalAdds2 = exp2Route[-1]
    for item in finalAdds1:
        stagesR1[-1].append([item, item.leapCent])
    for item in finalAdds2:
        stagesR2[-1].append([item, item.leapCent])
    occ = ""
    for i in occurances:
        occ += i + " "
    message = "The occurance(s) happen at transaction(s) " + occ + "\n"
    message += "From List One the steps to each occurance point are as follows: \n"
    i = 1
    for stage in stagesR1:
        if stage != stagesR1[-1]:
            message += "Stage "+ str(i) + "\n"
            for pair in stage:
                address1 = namer.lookupName(pair[0].hash, names)
                address2 = namer.lookupName(pair[2].hash, names)
                message += address1 + " and " + address2 + " share the transaction " + pair[1] + "\n"
            i +=1
    message += "Stage "+ str(i) + " \n"
    for final in stagesR1[-1]:
        tx = ""
        for trans in final[1]:
            tx += trans + " "
        address1 = namer.lookupName(final[0].hash, names)
        message += address1 + " hits the occurance transaction " + tx + "\n"
    message += "From List Two the steps to each occurance point are as follows: \n"
    i = 1
    for stage in stagesR2:
        if stage != stagesR2[-1]:
            message += "Stage ", i , "\n"
            for pair in stage:
                address1 = namer.lookupName(pair[0].hash, names)
                address2 = namer.lookupName(pair[2].hash, names)
                message += address1 + " and " + address2 + " share the transaction " + pair[1]
            i += 1
    message += "Stage " + str(i) + " \n"
    for final in stagesR2[-1]:
        tx = ""
        for trans in final[1]:
            tx += trans +" "
        address1 = namer.lookupName(final[0].hash, names)
        message += address1 + " hits the occurance transaction " + tx + "\n"

    return message



def demoSingle():
    address1 = "mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei" #input("Please enter the first address ")
    address2 = "mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W" #input("Please enter the second address ")
    return simpleOccuranceCheck(address1, address2)


def demoList():
    list1 = ["mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei"] #input("Please enter the first address ")
    list2 = ["moUkGQDCFqfbpbkETscTcX2fouLN8tnfQY"]#input("Please enter the second address ")
    return listOccuranceCheck(list1, list2)

def demoCheckOverLeaps():
    list1 = ["mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei"]#["2NDR6wnqrLpFZHwKbZhX2rSUzKxJ6uoKx3V"]
    list2 = ["moUkGQDCFqfbpbkETscTcX2fouLN8tnfQY"] #["2Mwq92dvkrQLsBGg7fRvifnuRVfMAbCFoSk"]
    maxSteps = 5
    return checkOverLeaps(list1,list2,maxSteps)

#print(demoSingle())
#print (demoList())
#occurance, occurances, l1Expansion, l2Expansion = demoCheckOverLeaps()
#print l1Expansion
print demoCheckOverLeaps()