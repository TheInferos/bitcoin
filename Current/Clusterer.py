import ClusterPackages.shadowChange
import ClusterPackages.multiAddress
import time
import os

def allHandle(arrayAddresses):
    changed = True
    nArray = arrayAddresses
    checked = []
    checked.append("2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF")
    sorted(nArray)
    temp = []
    f = open("Docs/Clusters/temp/"+ str(time.time())+nArray[0] +".txt", "w+")
    print os.getcwd()
    while changed:
        for address in nArray:
            if address not in (checked):
                print "multi " + address
                temp += ClusterPackages.multiAddress.multiaddress(address)
                print "shadow " + address
                temp += ClusterPackages.shadowChange.ShadowAddressCluster(address)
                temp = removeDupes(temp)
                print "sorting"
                temp = sorted(list(set(temp)))
                print "sorted"
                checked.append(address)
                message = ""
                print "writing"
                for ad in temp:
                    message += ad + " "
                f.write(message+"\n")
                print "writen"
        if temp == nArray:
            changed = False
        else:
            nArray = temp
    f.close()
    return nArray


def removeDupes(Array):
    return list(set(Array))

def clustererTest():
    print(allHandle(["2N3XwzC4U95SAU1fAk3YZvJjg444exttX8n"])) #not with huge list so looks good
    print "expected: 2N3XwzC4U95SAU1fAk3YZvJjg444exttX8n, 2Mt1HW1ABds5cF9Pq9uTmYH5jMGHSwcNnm4 "

#clustererTest()
#print(allHandle(["2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"])) # demo address for this as it shows lots of clustering addresses bar the fact that one of the adddresses needs to be cut
print(allHandle(["n3xtsoYapzcW2cSx1886f9KqkUmYNURcgY"]))
#print ("handle")

