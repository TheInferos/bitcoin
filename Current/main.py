import testingCode.Clusterer as Cluster
import namer
import occuranceCheck
import save

def main():
    pass

def clusterAddr(addrs, code):
    if code == "addr":
        #physical address
        addrs = Cluster.allHandle(addrs)
    elif code == "name":
        names = namer.lookupName()
    return addrs

def simpleCheckOccurance(addr1, addr2):
    occuranceCheck.simpleOccuranceCheck(addr1, addr2)

def multiCheckOccurance(list1, list2):
    occuranceCheck.listCompare(list1,list2) # need to create a list check

def saveAddresses(addresses):
    save.handle(addresses)

#print clusterAddr(["2N3XwzC4U95SAU1fAk3YZvJjg444exttX8n"], "addr")
saveAddresses(clusterAddr(["2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"], "addr"))
#main()