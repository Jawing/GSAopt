#!/usr/bin/python
"""main method"""

import numpy as np
import gameTable

finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
game2 = gameTable.Board(finalState)

## warning Game state will change
## when run. bfs dfs implemented on Obj
#game1.exploreBFS()
#game2.exploreBFS()

game1.exploreDFS()
game2.exploreDFS()
