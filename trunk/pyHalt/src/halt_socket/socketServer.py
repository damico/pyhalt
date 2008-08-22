# Echo server program
import socket
import os
from hostSec import hostSec

HOST = ''       # Symbolic name meaning the local host
PORT = 8081              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
if HOST == '':
    print 'Listening at localhost'
else:
    print 'Listening at '+HOST
    
s.listen(1)
data = '';
while 1:
    conn, addr = s.accept()
    sec = hostSec()
    print 'Trying to connect', addr[0], ':', addr[1]
    if sec.isValidClient(addr[0]):
        print 'Connected by', addr[0], ':', addr[1]
        data = conn.recv(1024)
        if data=='halt':
            os.system(data)
            conn.send(data)
        else:
            data = 'Command not found'
            print data
            conn.send(data)
    else:
        print 'Invalid host'
        conn.send('refused')