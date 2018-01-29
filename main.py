#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable
import search
finalState = [[0, 1, 2], [5, 4, 3]]
game2 = gameTable.Board(np.array(finalState))

assignment = [[1, 4, 2], [5, 3, 0]]
error = [[4, 4, 2], [5, 3, 0]]
test = [[3, 4, 5], [2, 0, 1]]
# HW to give an array of deepest path, need to try every config

game1 = gameTable.Board(np.array(test))

# NOTE uncomment to test out searching algorithm
# search.exploreBFS(game1)
# search.exploreDFS(game1)
# search.exploreIter(game1)
# search.exploreIterN(game1)
print("\nUniform Cost Search")
#search.exploreH(game1, gameTable.NoCost)
print("\nA* Search")
#search.exploreH(game1, gameTable.manhattanCost)
print("\nA* Search Weighted")
#search.exploreH(game1, gameTable.manhattanCost, search.find_neighbourW)
print("\nA* Search DOM")
# NOTE this is just like A* Search on a non weighted board
#search.exploreH(game1, gameTable.manhattanCostWeighted, search.find_neighbourW)
