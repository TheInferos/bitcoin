def checkSearch(testData):
    enter = True
    while enter:
        length = len(testData)
        if length == 5:
            textInput = "blockID"
            enter = False
        elif length == 16:
            textInput = "txHash"
            enter = False
        elif length == 12:
            textInput = "Address"
            enter = False
        else:
            print (testData)
            print ("please try again length not found to match criteria")
            testData = raw_input("Please insert a blockID (5 digits), Transaction Hash (16 Digits or an Address(12 digits) \n")
        return testData
def setInput(testData):
    testData =checkSearch(testData)
    return testData
def aquireInput():
    testData = raw_input("Please insert a blockID (5 digits), Transaction Hash (16 Digits or an Address(12 digits) \n")
    setInput(testData)
aquireInput()


