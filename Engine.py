from random import randint
from Other import Other


class Engine(object):

    def __init__(self, players: list, map_table: map):
        """

        :param players:
        :param map_table:
        """
        self.players = players
        self.map = map_table
        self.other = Other()

    def play(self):
        """

        :return:
        """
        # start player
        start_player = randint(0, 1)
        print(f"Player: {self.players[start_player].name} starts with symbol {self.players[start_player].symbol}.")
        # Show instructions
        self.map.plot_coordinates()
        # Show map
        self.map.plot_map()
        # Start playing!
        win = False
        tie = False
        turn = start_player
        turn_counter = 0
        while win is False and tie is False:
            # Get the map position
            map_position = self.players[turn].play()
            # Populate the map
            populated = self.map.populate_table(map_position, self.players[turn].symbol_num)
            # If operation was correct, update turn
            if populated:
                # The other player's turn
                turn = 1 - turn
                # Increment the turn counter
                turn_counter += 1
            # Show the map
            self.map.plot_map()
            # Verify for win condition
            win = self.win_condition(self.map.map_table)
            if turn_counter == 9:
                tie = True  # Tie condition
        print("The game has ended! Thanks for playing! :)")
        if tie and not win:
            print("Tie! No winners!")
        exit(0)

    def win_condition(self, matrix) -> list:  # Assuming players have 1 and -1 values
        # horizontal win condition
        win_h, who_symbol_num_h = self.horizontal_win_condition(matrix)
        # vertical win condition
        win_v, who_symbol_num_v = self.vertical_win_condition(matrix)
        # diagonal win condition
        win_d = self.diagonal_win_condition(matrix)
        return win_h or win_v or win_d

    def horizontal_win_condition(self, matrix):
        win = False
        who_symbol_num = None
        # horizontal win condition
        row_count = 0
        while (win is False) and (row_count <= len(matrix) - 1):
            total = sum(matrix[row_count])
            if abs(total) == 3:  # is there any winner?
                win = True
                who_symbol_num = self.other.sign_to_list_single_integer([total])
                self.who_has_won(who_symbol_num)
                return win, who_symbol_num
            else:
                row_count += 1
        return win, who_symbol_num

    def vertical_win_condition(self, matrix):
        # Transpose matrix
        transposed_matrix = list(map(list, zip(*matrix)))
        # Horizontal win condition
        win, who_symbol_num = self.horizontal_win_condition(transposed_matrix)
        return win, who_symbol_num

    def diagonal_win_condition(self, matrix):
        main_diag, second_diag = self.other.extract_diagonals(matrix)
        win_d1, who_symbol_num_d1 = self.horizontal_win_condition([main_diag])
        win_d2, who_symbol_num_d2 = self.horizontal_win_condition([second_diag])
        return win_d1 or win_d2

    def who_has_won(self, who_symbol_num):
        # Show that someone has won!
        players_to_sign = [player.symbol_num for player in self.players]
        print("{} has won!".format(self.players[players_to_sign.index(who_symbol_num)].name))


if __name__ == "__main__":
    from Map import Map
    from Player import Player

    # Create Map
    map_tab = Map()
    # Create players
    p1 = Player("selfstiano", "o")
    p2 = Player("Ignazio", "x")
    # generate a list of players
    players = [p1, p2]
    # Generate the engine
    engine = Engine(players, map_tab)

    print("Player names: {} and {}".format(*[player.name for player in players]))
    print("Player symbol: {} and {}".format(*[player.symbol for player in players]))
    print("Player symbol_to_num: {} and {}".format(*[player.symbol_num for player in players]))

    # Horizontal test - 1
    print("Horizontal tests")
    matrix = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
    engine.win_condition(matrix)

    # Horizontal test - 2
    matrix = [[-1, -1, -1], [0, 0, 0], [0, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 0], [-1, -1, -1], [0, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 0], [0, 0, 0], [-1, -1, -1]]
    engine.win_condition(matrix)

    # Vertical test - 1
    print("Vertical test")
    matrix = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
    engine.win_condition(matrix)

    # Vertical test - 2
    matrix = [[-1, 0, 0], [-1, 0, 0], [-1, 0, 0]]
    engine.win_condition(matrix)
    matrix = [[0, -1, 0], [0, -1, 0], [0, -1, 0]]
    engine.win_condition(matrix)
    matrix = [[0, 0, -1], [0, 0, -1], [0, 0, -1]]
    engine.win_condition(matrix)

    # Diagonal test - 1
    print("Diagonal test")
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    engine.win_condition(matrix)
    matrix = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    engine.win_condition(matrix)

    # Diagonal test - 2
    matrix = [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    engine.win_condition(matrix)
    matrix = [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]
    engine.win_condition(matrix)

    # Random tests
    print("Random Test: Not winning")
    matrix = [[0, 0, 0], [0, 0, 0], [1, -1, -1]]
    engine.win_condition(matrix)
    matrix = [[1, 0, -1], [0, 0, -1], [-1, 1, 1]]
    engine.win_condition(matrix)

    print("Single list of lists")
    matrix = [[1, 1, 1]]
    engine.win_condition(matrix)
