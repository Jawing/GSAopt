#!/usr/bin/python
"""define gameTable object"""

import numpy as np
#import math
#import pickle

#gameboard
class Board:
    #constructor 
    goal = np.array([[0, 1, 2], [5, 4, 3]])
    #TODO scalable goal location
    #ys = game.board.shape[0]
    #xs = game.board.shape[1]
    #goalLocation = [np.where(game.goal == x) for x in range(ys*xs))]  
    goalLocation = [(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
    def __init__(self, board):
        self.board = board
        self.emptyCell = np.where(self.board == 0)
    def moveDown(self):
        y,x = self.emptyCell[0][0],self.emptyCell[1][0]
        if (y < (self.board.shape[0]-1)):
            self.board[y,x],self.board[y+1,x] = self.board[y+1,x],self.board[y,x]
            self.emptyCell[0][0] +=1
        else: print("out of bounds")
        return
    def moveRight(self):
        y,x = self.emptyCell[0][0],self.emptyCell[1][0]
        if (x < (self.board.shape[1]-1)):
            self.board[y,x],self.board[y,x+1] = self.board[y,x+1],self.board[y,x]
            self.emptyCell[1][0] +=1
        else: print("out of bounds")
        return 
    def moveLeft(self):
        y,x = self.emptyCell[0][0],self.emptyCell[1][0]
        if (x > 0):
            self.board[y,x],self.board[y,x-1] = self.board[y,x-1],self.board[y,x]
            self.emptyCell[1][0] -=1
        else: print("out of bounds")
        return 
    def moveUp(self):
        y,x = self.emptyCell[0][0],self.emptyCell[1][0]
        if (y > 0):
            self.board[y,x],self.board[y-1,x] = self.board[y-1,x],self.board[y,x]
            self.emptyCell[0][0] -=1
        else: print("out of bounds")
        return 