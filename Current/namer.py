import os

def nameHandle(addr):
    named = passNamedAdds()
    addrs = lookupName(addr,named)
    return addrs

def passNamedAdds():
    names = {}
    f = open("Docs/NamedAddresses.txt", "r")
    lines = f.read().split("\n")
    for i in range(len(lines)):
        if lines[i] != "":
            row = lines[i].split(" ")
            names[row[0]] = " ".join(row[1:])
    f.close()
    return names


def updatSavedDict(dict):
    f2 = open("Docs/Named2.txt", "a+")
    for k in dict:
        f2.write(k + " " + dict[k] + "\n")
    f2.close()
    os.remove("Docs/NamedAddresses.txt")
    os.rename("Docs/Named2.txt", "Docs/NamedAddresses.txt")


def addToDict(address, name, dict):
    if address in dict:
        print "address already in dict"
    else:
        dict[address] = name
        updatSavedDict(dict)

def addressForName(name, names):
    addressList = []
    for ident in names:
        if names[ident] == name:
            addressList.append(ident)
    return addressList

def lookupName(addr, names):
    if addr in names:
        return names[addr]
    else:
        return addr

def testPassingNames():
    print "Testing Name passing "
    print "expecting mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei MadeUpWallet, mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W Totally Trustworth Source"
    print passNamedAdds()

def lookupTest():
    names = passNamedAdds()
    print "Lookup test"
    print "address 1: mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei, expected: MadeUpWallet"
    print lookupName("mzch8cQff4uhGnCwRQHpQgwnQZETUZq6ei", names)
    print "address 2: mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W, expected: Totally Trustworth Source"
    print lookupName("mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W", names)
    print "add3: mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7v, expected []"
    print lookupName("mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7v", names)


def addressTest():
    names = passNamedAdds()
    print "testing Address lookup given name"
    print "input: nametest, expected: 'mrFDZHRmPke6hFz77VYd716fVNetRDTS2M', '2Mvm7SKWxZrZMzjz9DvfXPmALVym3Mi98x4'"
    print addressForName("nametest", names)
    print "input: 'nametest ', expected: []"
    print addressForName("nametest ", names)
    print "input: 'Totally Trustworth Source', expected: 'mqeVPc7G6UcpBhknSB8qkaFZrAR6kpjP7W'"
    print addressForName("Totally Trustworth Source", names)


def updateDictTest():
    dict = passNamedAdds()
    print dict
    print "updateDict and addToDict test: first adding additional value"
    addToDict("123545678901234567890123456789012345","example", dict)
    dict = passNamedAdds()
    print "expecting '123545678901234567890123456789012345': 'example' to have been added"
    print dict
    print "testing if an address can be added twice"
    addToDict("123545678901234567890123456789012345", "example", dict)
    dict = passNamedAdds()
    print "expecting 'example': '123545678901234567890123456789012345' to have not been added plus message given before this"
    print dict


#updateDictTest()
# testPassingNames()
# lookupTest()
# addressTest()