# Echo client program
# import socket

# HOST = '127.0.0.1'    # The remote host
# PORT = 1338              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.send('Hello, world')
# data = s.recv(64)
# s.close()
# print('Received', repr(data))
# exit()


from player import *
# Debug (Run the player)
player = Player({
    'name': 'OtHellNo',
    'spaces': 8,
    'server': '127.0.0.1',
    'port': 1338,
    'debug': True
})

print(player.get_possible_moves())





