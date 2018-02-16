import os


class Game:
    # CurrentPlayer
    currentPlayer = False

    # History of the game moves
    history = {'global': [], 1: [], 2: []}

    # The board
    xSpaces = 0
    ySpaces = 0
    board = []

    # Init the game
    def __init__(self, x, y):
        self.currentPlayer = 1

        if x % 2 == 0 and x % 2 == 0:
            self.xSpaces = x
            self.ySpaces = y
            self.setup_board(x, y)

    # Board
    def setup_board(self, x, y):
        for i in range(x):
            self.board.append([])
            for j in range(y):
                self.board[i].append(0)

        self.board[int(x / 2)][int(y / 2)] = 1
        self.board[int(x / 2 - 1)][int(y / 2 - 1)] = 1
        self.board[int(x / 2 - 1)][int(y / 2)] = 2
        self.board[int(x / 2)][int(y / 2 - 1)] = 2
        return self

    def is_space_populated(self, x, y):
        if self.is_space_on_board(x, y) != True:
            return False

        return self.board[x][y] != 0

    def is_space_on_board(self, x, y):
        on_board = True
        if x > self.xSpaces:
            on_board = False

        if y > self.ySpaces:
            on_board = False

        return on_board

    def aquire_space(self, x, y, player):
        if self.is_space_on_board(x, y):
            if player == 1 or player == 2:
                self.board[x][y] = player
                return True
            return False

    # Game status
    def print_game(self):
        for i in range(self.xSpaces):
            print(self.board[i])

    def clear_display(self):
        os.system('cls')

    def print_game_status(self):
        self.clear_display()
        self.print_game()
        self.print_score()

    # Score
    def calculate_score(self):
        player_one = 0
        player_two = 0

        for i in range(self.xSpaces):
            for j in range(self.ySpaces):
                if self.board[i][j] == 1:
                    player_one += 1
                if self.board[i][j] == 2:
                    player_two += 1

        return {1: player_one, 2: player_two}

    def print_score(self):
        print ('Score: ')
        print (self.calculate_score())

    # Movement
    def get_possible_moves(self, player=0):
        if player == 0:
            player = self.currentPlayer

        moves = []
        # check board positions
        # calculate possible moves
        # return possibleMoves
        print('getPlayerMoves')
        # @TODO Add logic
        return moves

    # Rules
    def switch_player(self, player):
        self.currentPlayer = player
        return self

    def can_player_make_move(self):
        moves = self.get_possible_moves()
        if len(moves) > 0:
            print('canMakeMoves')
            # @TODO Add logic
        else:
            return False
