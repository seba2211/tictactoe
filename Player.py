from Other import Other


class Player(object):

    def __init__(self, name, symbol):
        self.name = name
        self.other = Other()
        self.symbol = symbol
        self.symbol_num = self.other.symbol_2_num(symbol)

    def play(self):
        input_position = input(f"- {self.name}, symbol = {self.symbol} - pos[x,y]> ")
        x_in = int(input_position[0]) - 1
        y_in = int(input_position[-1]) - 1

        return x_in, y_in
