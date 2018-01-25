"""main method"""

import numpy as np
import gameTable
#building an array
#define rules on the array
#search the array with bfs and

finalState = (0,1,2,5,4,3)

game1 = gameTable.Board((1,4,2,5,3,0))
game2 = gameTable.Board(finalState)
game1.print()

print(game1.is_final_state())
print(game2.is_final_state())



print(gameTable.exploredBoard)

if game1.board not in gameTable.exploredBoard: gameTable.exploredBoard[game1.board] = True

print(gameTable.exploredBoard)


finalState[0]=finalState[1]