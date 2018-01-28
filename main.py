#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable
import search
finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
game2 = gameTable.Board(finalState)


# Breadth First Search
print("\nBreadth First Search")
search.explore(game1, search.SearchQueue, gameTable.NoCost)
# Uniform Cost Search
print("\nUniform Cost Search")
search.explore(game1, search.SearchHeap, gameTable.NoCost)
# Depth First Search
print("\nDepth First Search")
search.explore(game1, search.SearchStack, gameTable.NoCost)
# Iterative Depth First Search

print("\nIterative Depth First Search")
search.exploreiter(game1, gameTable.NoCost)
