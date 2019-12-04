from Other import Other
from textwrap import dedent


class Map(object):
    def __init__(self):
        # initial map
        self.map_len = 3
        self.map_table = [[0 for i in range(0, self.map_len)] for i in range(0, self.map_len)]
        self.other = Other()
        # print(self.other.num_to_symbol_list(self.map_table[1]))

    def plot_map(self):  # plot the map
        print("Current Map")
        print("_" * 7)
        for i in range(0, self.map_len):
            print("|{}|{}|{}|".format(*self.other.num_to_symbol_list(self.map_table[i])))
        print("_" * 7)

    def plot_coordinates(self):  # plot the coordinates
        print("These are the supported coordinates: ")
        print("-" * 22)
        print("_" * 22)
        for i in range(0, self.map_len):
            print("|{}|{}|{}|".format(*[[i + 1, 1], [i + 1, 2], [i + 1, 3]]))
        print("_" * 22)
        print("-" * 22)
        print(dedent("""
        Don't use parentheses, is enough using, e.g.: 
        * 1,3 for [1,3]
        * 1.3 for [1,3]
        or even:
        * 13 for [1,3]
        """))

    def populate_table(self, map_position, value):  # 'inhabit' the map
        # unpack the map position
        map_x, map_y = map_position

        # If the coordinates are inside the map
        if (map_x in range(0, self.map_len)) and (map_y in range(0, self.map_len)):
            # If the map position is empty
            if self.map_table[map_x][map_y] == 0:
                self.map_table[map_x][map_y] = value
                return True
            else:
                print(f"Position {[coord + 1 for coord in map_position]} already occupied!")
                return False
        else:
            print("Invalid position x = {}, y = {}".format(*[coord + 1 for coord in map_position]))
            self.plot_coordinates()
            return False

    def present_yourself(self):
        welcome_str = "Welcome to the Tic Tac Toe game!"
        print("#" * len(welcome_str))
        print(welcome_str)
        print("#" * len(welcome_str))


if __name__ == '__main__':
    m = Map()
    m.plot_map()
    m.plot_coordinates()
