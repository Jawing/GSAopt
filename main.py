#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable
import search
finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
game2 = gameTable.Board(finalState)

search.exploreBFS(game1)
search.exploreBFS(game2)
search.exploreDFS(game1)
search.exploreDFS(game2)



