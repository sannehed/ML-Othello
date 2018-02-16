# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 1338              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(64)
    if not data:
        break
    conn.send(data)
conn.close()
exit()

# Echo client program
HOST = '127.0.0.1'    # The remote host
PORT = 1338              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(64)
s.close()
print('Received', repr(data))
exit()