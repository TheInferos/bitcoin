import ClusterPackages.shadowChange
import ClusterPackages.multiAddress
import time

def allHandle(arrayAddresses):
    changed = True
    nArray = arrayAddresses
    checked = []
    checked.append("2N8hwP1WmJrFF5QWABn38y63uYLhnJYJYTF")
    sorted(nArray)
    temp = []
    print str(time.time())
    #f = open("Docs/Clusters/temp/"+ str(time.time())+".txt", "w+")
    #f = open("Current/Docs/Clusters/temp/123", "w+")
    while changed:
        for address in nArray:
            if address not in (checked):
                #print address
                print "multi"
                temp += ClusterPackages.multiAddress.multiaddress(address)
                print "shadow"
                temp += ClusterPackages.shadowChange.ShadowAddressCluster(address)
                temp = removeDupes(temp)
                print "sorting"
                sorted(temp)
                print "sorted"
                checked.append(address)
                message = ""
                print "writing"
                for ad in nArray:
                    message += ad + " "
                f.write(message+"\n")
                print "writen"
        if temp == nArray:
            changed = False
        else:
            nArray =temp
            #print nArray
    f.close()
    return nArray


def removeDupes(Array):
    return list(set(Array))

print(allHandle(["2N3XwzC4U95SAU1fAk3YZvJjg444exttX8n"])) #not with huge list so looks good
#print(allHandle(["2N6TtLayzyLr6B764arv1UGGLfTpic2cWZN"]))
#print ("handle")

