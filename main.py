"""main method"""

import numpy as np
import gameTable
#building an array
#define rules on the array
#search the array with bfs and
board1 = np.array([[1, 4, 2], [5, 3, 0]])
board2 = np.array([[0, 1, 2], [5, 4, 3]])
game1 = gameTable.Board(board1)
game2 = gameTable.Board(board2)
game1.print()

print(game1.is_final_state())
print(game2.is_final_state())


board_key = tuple(map(tuple,game1.board))
if board_key not in gameTable.exploredBoard: gameTable.exploredBoard[board_key] = True

print(gameTable.exploredBoard)


