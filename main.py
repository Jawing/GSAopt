#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable
import search
finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
game2 = gameTable.Board(finalState)

search.explore(game1, search.BinaryHeap, gameTable.NoCost)
search.explore(game1, search.BinaryHeap, gameTable.manhattanCost)

search.explore(game1, search.BFS, gameTable.NoCost)

search.explore(game2, search.BFS, gameTable.NoCost)
search.explore(game1, search.DFS, gameTable.NoCost)
search.explore(game2, search.DFS, gameTable.NoCost)
