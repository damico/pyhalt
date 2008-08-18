from properties import CONFIG_FILE

class fileUtils(object):
    def __init__(self):
        self
    def getFile(self):
        f = open(CONFIG_FILE)
        validClients = list()
        for line in f:
            validClients.append(line)
        f.close()
        return validClients   