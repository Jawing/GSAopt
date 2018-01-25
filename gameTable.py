#!/usr/bin/python
"""define gameTable object"""

import numpy as np
import math
import pickle
from collections import deque

#gameboard
class Board:
    #constructor 
    def __init__(self, board):
        self.board = board
        #key mapped as tuple
        self.boardKey = tuple(map(tuple,self.board))
        self.emptyCell = np.where(self.board == 0)
        #explored board for the object instance
        #goes within explore?
        self.exploredBoard = {}
        #show path taken
        self.path = []

    #searching algorithm
    def exploreBFS(self):
        step = 0 
        queue = deque([self.board])
        #if start state is final
        if self.is_final_state():
            return self.board

        # keep looping until final state is reached
        while queue:
            # pop shallowest node (first node) from queue
            self.board = queue.popleft()
            self.boardKey = tuple(map(tuple,self.board))
            self.emptyCell = np.where(self.board == 0)
            #self.path = self.path.append(self.board)
            # debug:show steps and board pathing
            step += 1
            print("step:", step)
            self.print()

            # add neighbours of node to queue
            neighbours = self.find_neighbor()
            for neighbour in neighbours:
                # make sure not explore repeated paths
                if  tuple(map(tuple,neighbour)) not in self.exploredBoard:
                    #keep track of path
                    #path.append(neighbour)
                    queue.append(neighbour)
                    # return path if neighbour is goal
                    if np.array_equal(neighbour,[[0, 1, 2], [5, 4, 3]]):
                        return neighbour
            # add node to list of checked nodes
            self.exploredBoard[self.boardKey] = True
        return 

    #find valid moves or board states
    def find_neighbor(self):

        #can optimize by saving previous move!!!
        #valid move table
        x,y=self.emptyCell

        def moveDown():
            board = np.copy(self.board)
            board[x,y],board[x+1,y] = board[x+1,y],board[x,y]
            return board
        def moveRight():
            board = np.copy(self.board)
            board[x,y],board[x,y+1] = board[x,y+1],board[x,y]
            return board
        def moveLeft():
            board = np.copy(self.board)
            board[x,y],board[x,y-1] = board[x,y-1],board[x,y]
            return board
        def moveUp():
            board = np.copy(self.board)
            board[x,y],board[x-1,y] = board[x-1,y],board[x,y]
            return board
        if x[0] == 0 and y[0] == 0:
            return [moveDown(), moveRight()]
        elif x[0] == 0 and y[0] == 1:
            return [moveDown(), moveRight(), moveLeft()]
        elif x[0] == 0 and y[0] == 2:
            return [moveDown(), moveLeft()]
        elif x[0] == 1 and y[0] == 0:
            return [moveRight(), moveUp()]
        elif x[0] == 1 and y[0] == 1:
            return [moveRight(), moveUp(), moveLeft()]
        elif x[0] == 1 and y[0] == 2:
            return [moveUp(), moveLeft()]
        else: return print("error in find_neighbor")
        

    #print board state
    def print(self):
        print("board:\n",self.board)
        print("emptyCell:\n",self.emptyCell,"\n")
        return 
    
    #check if it is final state of game
    def is_final_state(self):
        return np.array_equal(self.board,[[0, 1, 2], [5, 4, 3]])


