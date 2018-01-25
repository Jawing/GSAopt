"""main method"""

import numpy as np
import gameTable
#building an array
#define rules on the array
#search the array with bfs and

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l[::2], l[1::2] = l[1::2], l[::2]

print(l)

finalState = (0,1,2,5,4,3)

game1 = gameTable.Board((0,4,2,5,3,1))
game2 = gameTable.Board(finalState)

game1.print()
game1.exploreBFS()