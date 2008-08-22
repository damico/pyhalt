from fileUtils import fileUtils

class hostSec(object):
    
    def __init__(self):
        self 
    def isValidClient(self,client):
        fU = fileUtils()
        validClients =  fU.getFile()
        for i in validClients:
            if client in validClients: key = True
            else: key = False
        return key