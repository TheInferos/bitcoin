import os

def nameHandle(name):
    named = passNamedAdds()
    addrs = lookupName(name,named)
    return addrs

def passNamedAdds():
    names = {}
    f = open("Docs/NamedAddresses.txt", "r")
    lines = f.read().split("\n")
    for i in range(len(lines)):
        if lines[i] != "":
            row = lines[i].split(" ")
            #print (row[0], row[1])
            names[row[0]] = row[1]
    f.close()
    return (names)


def updatSavedDict(dict):
    f2 = open("Docs/Named2.txt", "a+")
    for k in dict:
        f2.write(k + " " + dict[k] + "\n")
    f2.close()
    os.remove("Docs/NamedAddresses.txt")
    os.rename("Docs/Named2.txt", "Docs/NamedAddresses.txt")


def addToDict(address, name, dict):
    #add a checker in here
    dict[address] = name
    updatSavedDict()


def lookupName(name, names):
    if name in names:
        return names[name]
    else:
        return []

