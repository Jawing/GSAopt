"""main method"""

import numpy as np
import gameTable
#building an array
#define rules on the array
#search the array with bfs and

finalState = (0,1,2,5,4,3)

game1 = gameTable.Board((0,4,2,5,3,1))
game2 = gameTable.Board(finalState)
game1.print()

print(game1.is_final_state())
print(game2.is_final_state())



print(game1.exploredBoard)

if game1.board not in game1.exploredBoard: game1.exploredBoard[game1.board] = True

print(game1.exploredBoard)
print(game2.exploredBoard)
print(game1.board[1:3])
game1.moveDowntest()
game1.print()