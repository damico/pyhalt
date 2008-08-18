# Echo client program
import sys
import socket


    # The remote host
PORT = 8081           # The same port as used by the server

host = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, PORT))
inputS = sys.argv[1]
s.send(inputS)
data = s.recv(1024)
s.close()
print 'Received', repr(data)