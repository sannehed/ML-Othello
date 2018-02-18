import time
import socket
import struct
import random

from game import Game


class Player:
    name = False
    spaces = False
    server = False
    port = False
    buffer_size = False
    max_receive_errors = False
    receive_errors = False
    debug = False
    default_settings = {
        'name': 'OtHellNo',
        'spaces': 8,
        'server': '127.0.0.1',
        'port': 1338,
        'buffer_size': 64,
        'max_receive_errors': 10,
        'receive_errors': 0,
        'debug': True
    }
    errors = []
    id = False
    game = False
    socket = False

    def debugger(self, msg):
        if self.debug:
            print('DEBUGGER: [{}] -> {}'.format(*(time.strftime("%Y-%m-%d %H:%M:%S"), msg)))

    # Init
    def __init__(self, settings={}):
        self.process_settings(settings)

        self.game = Game(self.spaces, self.spaces)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.debugger('Player Initiated.')

    def process_settings(self, settings):
        default_settings = self.default_settings

        for (key, value) in default_settings.items():
            if hasattr(settings, key):
                setattr(self, key, settings[key])
            else:
                setattr(self, key, value)
            self.debugger('Setting "{}" set to "{}"'.format(*(key, getattr(self, key))))

    def log_error(self, note):
        timestamp = time.strftime("%Y-%m-%d %H:%M")
        self.errors.append({'timestamp': timestamp, 'error': note})
        self.debugger('An error has been logged. ({})'.format(note))

    def quit(self):
        if self.has_connection():
            self.close_connection()

        return self

    # Network
    def connect_to_lobby(self):
        server_address = (self.server, self.port)
        self.debugger('connecting to {} port {}'.format(*server_address))
        try:
            self.socket.connect(server_address)
            self.send_data(self.name)
        except Exception as e:
            self.log_error(e)

    def has_connection(self):
        has_connection = False

        # @TODO Add logic

        return has_connection

    def close_connection(self):
        try:
            self.socket.close()
        except Exception as e:
            self.log_error(e)

    def receive_data(self):
        retry = False
        should_exit = False

        try:
            data = self.socket.recv(self.buffer_size)
        except Exception as e:
            self.log_error(e)
            data = False

        if data:
            unpacked_data = self.unpack_data(data)
            if unpacked_data:
                self.update_game(unpacked_data)
            else:
                retry = self.receive_errors < self.max_receive_errors
                should_exit = self.receive_errors >= self.max_receive_errors

        if retry:
            self.receive_errors += 1
            time.sleep(5)
            self.receive_data()

        elif should_exit:
            self.quit()

    def unpack_data(self, data):
        try:
            unpacked_data = struct.unpack('17c', data)
        except Exception as e:
            self.log_error(e)
            unpacked_data = False

        return unpacked_data

    def send_data(self, data):
        try:
            self.socket.send(data)
        except Exception as e:
            self.log_error(e)

    # Game
    def update_game(self, data):
        self.receive_errors = 0
        self.debugger('update_game')
        # @TODO Add logic

    def make_move(self):
        moves = self.game.get_possible_moves()
        player_move = self.select_move(moves)
        return self.game.aquire_space(player_move['x'], player_move['y'], self.id)

    def select_move(self, moves):  # @TODO Add correct logic
        number_of_moves = len(moves)
        the_move = random.randint(0, number_of_moves-1)
        return the_move

# Debug (Run the player)
player = Player()
player.connect_to_lobby()


# ---===( Timeline )===--- #
#
# 1. Servern startas
#
# 2. Klient 1 kopplar upp sig och väntar på svar från servern att det är dags att börja
#
# 3. Klient 2 kopplar upp sig och väntar på svar från servern att det är dags att börja
#
# 4. Servern säger "Det är dags att börja. Klient 1 kör" och skickar med statusen på brädet
#
# 5. Klient ett skickar ett move
#
# 6. Servern kollar om man får göra movet och skickar tillbaka till klienten att movet är legit.
#
# 7. a) Klient 1 väntar nu på att servern ska säga att det är dags för ett nytt move
#
# 7. b) Servern säger till Klient 2 att göra sitt move och skickar med statusen på brädet
#
# 8. Klient ett skickar ett move
#
# 9. Servern kollar om man får göra movet och skickar tillbaka till klienten att movet är legit.