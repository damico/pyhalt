from properties import configFile

class hostSec(object):
    
    def __init__(self):
        self 
    def isValidClient(self,client):
        f = open(configFile)
        validClients = list();
        for line in f:
            validClients.append(line)
        f.close()   
        
        for i in validClients:
            if client in validClients: key = True
            else: key = False
        
        return key