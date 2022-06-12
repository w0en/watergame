import random
import pprint as pp
from class_entry import Entry
from class_tube import Tube
from class_game import Game


def generate_game(tube_list):
    return Game(tube_list)


def generate_random_game(tube_sizes):
    return None
    #Need to find out mathematical properties. Currently thinking of having tubes in different sizes represented as list of tuples.
    #For example, [(3, 4), (1, 2)] generates 3 tubes with 4 entries, and 1 tube with 2 entries. Need to figure out how to generate the empty tubes too.

tube0 = Tube(4, [])
tube1 = Tube(4, [])
tube2 = Tube(4, [Entry(2, False), Entry(2, False), Entry(2, False), Entry(2, False)])
tube3 = Tube(4, [Entry(3, False), Entry(3, False), Entry(3, False), Entry(3, False)])
tube4 = Tube(4, [Entry(4, False), Entry(4, False), Entry(4, False), Entry(4, False)])
tube5 = Tube(4, [Entry(5, True), Entry(5, False), Entry(6, False), Entry(6, False)])
tube6 = Tube(4, [Entry(6, False), Entry(6, False), Entry(5, False), Entry(5, False)])

print("============== NEW RUN START ==============")
game = generate_game([tube0, tube1, tube2, tube3, tube4, tube5, tube6])
print(game)
pp.pprint(game.tubes)
"""
print("Wrong Move 1: 0 -> 1")
game.pour(game.tubes[0], game.tubes[1])
print("Wrong Move 2: 0 -> 2")
game.pour(game.tubes[0], game.tubes[2])
"""
print("Move 1: 5 -> 1")
game.pour(game.tubes[5], game.tubes[1])
print("Move 2: 6 -> 5")
game.pour(game.tubes[6], game.tubes[5])
print("Move 3: 1 -> 6")
game.pour(game.tubes[1], game.tubes[6])
print(game)
game.pour(game.tubes[5], game.tubes[1])
print(game)
game.pour(game.tubes[1], game.tubes[5])
print(game)
pp.pprint(game.tubes)
print("============== NEW RUN END ==============")