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
