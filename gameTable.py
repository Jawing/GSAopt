#!/usr/bin/python
"""define gameTable object"""

import numpy as np
import math
import pickle
from collections import deque

#gameboard
class Board:
    #boards that have been explored in searching
    exploredBoard = {}
    #constructor 
    def __init__(self, board):
        #current board state
        self.board = board
        #current empty cell location
        self.emptyCell = self.board.index(0)

    #searching algorithm
    def explore(self):
        ##???queue
        queue = deque([self.board])

        step = 0 
        # keep looping until final state is reached
        while not self.is_final_state:
            # debug:show steps and board pathing
            step += 1
            print("step:", step, "\nboardPath:", exploredBoard)

            # pop shallowest node (first node) from queue
            # change the board state TO IMPLEMENT!!
            self.board = queue.popleft()
            # make sure not explore repeated paths
            if  self.board not in exploredBoard:
                # add node to list of checked nodes
                exploredBoard[self.board] = True
                
                """
                need to implement neighbour function tuple list
                neighbours = graph[node]
                """
                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return 
    
    #find valid moves or board states
    def find_neighbor(self)
        moveUpTable = {0:}

    #print board state
    def print(self):
        print("board:\n",self.board)
        print("emptyCell:\n",self.emptyCell)
        return 
    
    #check if it is final state of game
    def is_final_state(self):
        return self.board == (0,1,2,5,4,3)
    def is_explored(self,exploredSet):
        return exploredSet(self.board)


