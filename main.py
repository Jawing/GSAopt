#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable
import search
finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
game2 = gameTable.Board(finalState)



search.exploreBFS(game1)

search.exploreDFS(game1)

print("Uniform Cost Search")
search.exploreH(game1, gameTable.NoCost)

print("A* Search")
search.exploreH(game1, gameTable.manhattanCost)

print("A* Search Weighted")
search.exploreH(game1, gameTable.manhattanCost, search.find_neighbourW)
