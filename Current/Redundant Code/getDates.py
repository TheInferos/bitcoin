import requests

def getBlockHash(bkNumber):
    request = "https://test-insight.bitpay.com/api/block-index/" + str(bkNumber)
    res = requests.get(request)
    return res.json()["blockHash"]

def parseInfo():
    f = open("Docs/BlockTimes.txt", "r+")
    list =f.read().split("\n")
    f.close()
    if len(list) != 0:
        lastLine = list[-1].split(" ")
        return eval(lastLine[0])
    else:
        return -1

def requestInfo(bkHash):
    request = "https://test-insight.bitpay.com/api/block/" + str(bkHash)
    res = requests.get(request)
    resJson = res.json()
    if "nextblockhash" in resJson:
        return resJson["height"] ,resJson["time"], resJson["nextblockhash"]
    else:
        return resJson["height"], resJson["time"], -1

def writeTimes(f, bkId, time):
    message = "\n"+ str(bkId) + " " + str(time)
    f.write(message)

def main():

    lastBlock = parseInfo()
    lastBlock = 1 + int(lastBlock)
    f = open("Docs/BlockTimes.txt", "a")
    bkHash = getBlockHash(lastBlock)
    height, time, nextHash = requestInfo(bkHash)
    writeTimes(f, height, time)

main()