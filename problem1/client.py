import socket
import sys
s = socket.socket()
s.connect(('localhost', 8817))
s.send(bytes('hello', 'utf-8'))  
data = s.recv(1024) 
print ('received ', int.from_bytes(data, byteorder='big')) 
s.close()
