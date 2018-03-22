# Author: UP792564

def checkSearch(testData):
    enter = True
    while enter:
        length = len(testData)
        if length <= 6: #needs changing to current latest block
            textInput = "blockID"
            enter = False
        elif length == 64:
            textInput = "txHash"
            enter = False
        elif length == 34:
            textInput = "Address"
            enter = False
        else:
            #print (testData)
            print ("please try again length not found to match criteria")
            testData = input("Please insert a blockID (5 digits), Transaction Hash (16 Digits or an Address(12 digits) \n")
        return testData, textInput

def setInput(testData):
    testData =checkSearch(testData)
    return testData

def aquireInput():
    testData = input("Please insert a blockID (5 digits), Transaction Hash (16 Digits or an Address(12 digits) \n")
    setInput(testData)
aquireInput()


# sample transaction id ( wiohtout added in spaces) = 64chars d60a1 60ef3 3efcf 09c75 598f5 ce29b 5c1dc 2eb61 31a71 5a234 87861 12192 6e7a
# sample Address (without added in spaces) = 34 14KYw Hhnx5 QcACT 31cd2 AfhuG D8evx JCV4