"""main method"""

import numpy as np
import gameTable
#building an array
#define rules on the array
#search the array with bfs and


finalState = np.array([[0, 1, 2], [5, 4, 3]])

game1 = gameTable.Board(np.array([[1, 4, 2], [5, 3, 0]]))
print(game1.emptyCell)

game2 = gameTable.Board(finalState)

game1.print()
print(game1.exploreBFS())