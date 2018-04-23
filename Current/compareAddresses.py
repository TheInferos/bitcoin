from Objects import Address as addr
import requests

def simpleCompare(addr1Hash, addr2Hash):
    addr1 = addr.Address(addr1Hash)
    addr2 = addr.Address(addr2Hash)
    if len(addr1.tx) <= len(addr2.tx):
        shorter = addr1
        compAddr = addr2
    else:
        shorter = addr2
        compAddr = addr1
    occurance = []
    for transx in shorter.tx:
        if transx in compAddr.tx:
            occurance.append(str(transx))
    return occurance

def listCompare(list1, list2):
    addresses1 = []
    list1Trans = []
    addresses2 = []
    list2Trans = []
    for addr1 in list1:
        address = addr.Address(addr1)
        addresses1.append(address)
        for trans in address.tx:
            list1Trans.append(trans)
    list1Trans = sorted(list(set(list1Trans)))
    for addr2 in list2:
        address = addr.Address(addr2)
        addresses2.append(address)
        for trans in address.tx:
            list2Trans.append(trans)
    list2Trans = sorted(list(set(list2Trans)))
    if len(list1Trans) <= len(list2Trans):
        shorter = list1Trans
        compAddr = list2Trans
    else:
        shorter = list2Trans
        compAddr = list1Trans
    occurance = []
    for transx in shorter:
        if transx in compAddr:
            occurance.append(str(transx))
    return occurance

def simpleTest():
    print "Simple compare test"
    print "Expected value: 'c29434ad307c7aa0258d1a85f8cc9cec2d064239350eb4d4e96a4ede090812ce' test October 17"
    print simpleCompare("n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7", "2N672VWCiPhob46jEVrpohd47Xqg7koufug")
    print "No Occurance Check Expected Value []"
    print simpleCompare("n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7", "muh7aXhqSc3FDTG7nkyamS4AFSxcL4gWAF")


def listTest():
    print "list compare test"
    print "expected Value  'c29434ad307c7aa0258d1a85f8cc9cec2d064239350eb4d4e96a4ede090812ce' October17"
    print(listCompare(["n2BAtxE3FgRPkCbDQbh2WymEwqUCiPB9B7"], ["2N672VWCiPhob46jEVrpohd47Xqg7koufug"]))
    print "List Compare (no connection)"
    print(listCompare(["muh7aXhqSc3FDTG7nkyamS4AFSxcL4gWAF"], ["2N672VWCiPhob46jEVrpohd47Xqg7koufug"]))


#listTest()
#simpleTest()