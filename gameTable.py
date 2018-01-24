#!/usr/bin/python
"""define gameTable object"""

import numpy as np
import math
import pickle

exploredBoard = {}
#gameboard
class Board:
    def __init__(self, board): #constructor 
        self.board = board
        self.emptyCell = np.where(board == 0)

    def moveUp(self):
        raise NotImplementedError
    def phase(self):
        pass

        #print board state
    def print(self):
        print("board:\n",self.board)
        print("emptyCell:\n",self.emptyCell)
        return 
        #check final state of game
    def is_final_state(self):
        return np.array_equal(self.board,[[0, 1, 2], [5, 4, 3]])
    


def is_explored(game, exploredSet):
    return exploredSet(tuple(game.board))


