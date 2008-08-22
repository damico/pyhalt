# Echo client program
import sys
import socket
from fileUtils import fileUtils


    # The remote host
PORT = 8081           # The same port as used by the server
host = sys.argv[2]
inputS = sys.argv[1]

def sendMessage(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(inputS)
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)

if host == '0.0.0.0':
    fU = fileUtils()
    validClients = fU.getFile()
    for i in validClients:
        print 'sending multiple '+inputS+' commands! ==> '+i
        try:
            sendMessage(i)
        except:
            print 'no server at '+i
else:
    sendMessage(host)

