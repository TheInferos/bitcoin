import os
def passNamedAdds():
    dict = {}
    f = open("Docs/NamedAddresses.txt", "r")
    lines = f.read().split("\n")
    for i in range(len(lines)):
        if lines[i] != "":
            row = lines[i].split()
            dict [row[0]] = row[1]
    f.close()
    return (dict)

def updatSavedDict(dict):
    f2 = open("Docs/Named2.txt", "a+")
    for k in dict:
        f2.write(k + " " + dict[k] + "\n")
    readF = f2.read()
    f2.close()
    os.remove("Docs/NamedAddresses.txt")
    os.rename("Docs/Named2.txt", "Docs/NamedAddresses.txt")

def addToDict(address, name, dict):
    #add a checker in here
    dict[address] = name
    updatSavedDict()
