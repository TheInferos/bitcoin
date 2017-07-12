from bitcoin.Current import namer
from bitcoin.Current import searchHandler

namedAddresses = namer.passNamedAdds()
namer.updatSavedDict(namedAddresses)
searchHandler.searchSetup()
