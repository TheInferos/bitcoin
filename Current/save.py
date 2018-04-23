def handle(originaladdresses):
    sortedAddresses =sorted(list(set(originaladdresses)))
    for addr in originaladdresses:
        fName = getFileName(addr)
        message = makeMessage(sortedAddresses, addr)
        writeMessage(message,fName)

def writeMessage(message,fileName):
    f = open(fileName, "r+")
    lines = f.read()
    splits = lines.split("\n")
    f.close()
    f = open(fileName, "w+")
    if len(lines)> 0:
        FullWrite = ""
        messadded = False
        for line in splits:
            firstLine = line.split(" ")
            firstMessage = message.split(" ")
            if firstLine[0] == firstMessage[0]:
                #print "3 " + message
                FullWrite += message + "\n"
                messadded = True
            else:
                FullWrite += line + "\n"
        if messadded == False:
            FullWrite += message
        print(FullWrite[-4])
        f.write(FullWrite)
    else:
        f.write(message)
    f.close()


def getFileName(addr):
    return str("Docs/Clusters/"+addr[0:5]+".txt")

def makeMessage(makesaddresses,currentAddress):
    message = currentAddress
    address = checkIfExisting(makesaddresses, currentAddress)
    for addrs in address:
        if addrs != currentAddress:
            message += " " + addrs
    return message


def checkIfExisting(addresses,currentAddress):
    fOrignal = open(getFileName(currentAddress), "a+")
    f = fOrignal.read()
    fOrignal.close()
    if len(f) > 0:
        lines = f.split("\n")
        for line in lines:
            existLine = line.split(" ")
            if existLine[0] == currentAddress:
                for eline in existLine:
                    addresses.append(eline)
                addresses= list(set(addresses))
                addresses.remove(currentAddress)
                addresses = [currentAddress] + sorted(addresses)
                return addresses
    return addresses

def addAddresses(addresses, code):
    for addr1 in addresses:
        message = str(addr1) + " "
        for addr2 in addresses:
            if addr1 != addr2:
                 message += addr2 + " " + code + " "
    return message

def moduleTest():
    address = ["abcdefghijklmnopqrstuvwxyz123456789","abcdefghijklmnopqrstuvwxyz123456788", "abcdefghijklmnopqrstuvwxyz123456787", "9bcdefghijklmnopqrstuvwxyz12345678a"]
    handle(address)
moduleTest()
