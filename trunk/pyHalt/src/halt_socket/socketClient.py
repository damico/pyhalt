# Echo client program
import sys
import socket
import fileUtils


    # The remote host
PORT = 8081           # The same port as used by the server
host = sys.argv[2]
inputS = sys.argv[1]

if host == '0.0.0.0':
    validClients = fileUtils.getFile()
    for i in validClients:
        sendMessage(i)
        print 'sending multiple '+inputS+' commands! '+'['+i+']'
else:
    sendMessage(host)

def sendMessage(self, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, PORT))
    s.send(inputS)
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)