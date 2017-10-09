import socket
import sys
i = 0
s = socket.socket()
s.bind(('localhost', 8817))
while True:
    s.listen(1)
    conn, addr = s.accept()
    i = i + 1
    data = conn.recv(1024)
    print('clients', i)
    conn.send(bytes([i]))
    conn.close()
