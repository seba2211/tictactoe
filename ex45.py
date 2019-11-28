# ex45

# My own game - tic tac toe

"""
# DESCRIPTION
--- Classes 

Map --> 9 positions
	- State -> 0/1 ('x' or 'o')

Players --> 2 players
	- Name: Input at the beginning

Engine --> Turn assignment
	- WinCondition

--- Mechanics ---

* 2 players are identified
* Select 1 randomly to start
* Play
* Finish condition

"""
from Map import Map
from Engine import Engine
from Player import Player
from random import randint

# Symbol List - random selection
symbols = ["x", "o"]
rand_index = randint(0, 1)
s1 = symbols.pop(rand_index)
s2 = symbols.pop()

if __name__ == "__main__":
	# Create Map
	map_table = Map()
	# Game presentation
	map_table.present_yourself()
	# Create players
	p1_name = input("Insert the name of the first player: ")
	p2_name = input("Insert the name of the second player: ")
	p1 = Player(p1_name, s1)
	p2 = Player(p2_name, s2)
	# generate a list of players
	players = [p1, p2]
	# Generate the engine
	engine = Engine(players, map_table)

	print("Player names: {} and {}".format(*[player.name for player in players]))
	print("Player symbols: {} and {}".format(*[player.symbol for player in players]))

	# Play!
	engine.play()
