from bitcoin.Current.Objects import Address
from bitcoin.Current.Objects import Block
from bitcoin.Current.Objects import Transaction

def searchSetup(searchBy, searchMaterial):
    if searchBy == "blockId":
        SearchByBlock(searchMaterial)
    #elif searchBy =="TransactionId":
    #   print("trans")
    elif searchBy == "Address":
        SearchByAddress(searchMaterial)
    else:
        print( "errrr whoops please report the error and i will get back to you")
def SearchByBlock(blockID):
    block = Block.Block(blockID)
    print (block.blockID)

def SearchByAddress(hash):
    address = Address.Address(hash)
    print(address.hash)
