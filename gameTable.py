#!/usr/bin/python
"""define gameTable object"""

import numpy as np
import math
import pickle
from collections import deque

#gameboard
class Board:
    #boards that have been explored in searching
    
    #validMoves down right up left
  

    #constructor 
    def __init__(self, board):
        #current board state
        self.board = board
        #current empty cell location
        self.emptyCell = self.board.index(0)
        #explored board for the object instance
        #goes within explore?
        self.exploredBoard = {}

    #searching algorithm
    def exploreBFS(self):

        queue = deque([self.board])

        step = 0 
        #if start state is final
        if self.is_final_state():
            return self.board
        # keep looping until final state is reached
        while queue:
           
            # pop shallowest node (first node) from queue
            self.board = queue.popleft()
            self.emptyCell = self.board.index(0)
            
            # debug:show steps and board pathing
            step += 1
            print("step:", step, "\n")
            self.print()


            # make sure not explore repeated paths
            if  self.board not in self.exploredBoard:
                
                neighbours = self.find_neighbor()
                # add neighbours of node to queue
                
                for neighbour in neighbours:
                    #keep track of path bugged!!!
                    #path = list(self.board)
                    #path.append(neighbour)

                    queue.append(neighbour)
                    # return path if neighbour is goal
                    if neighbour == (0,1,2,5,4,3):
                        return neighbour
                # add node to list of checked nodes
                self.exploredBoard[self.board] = True
        return 
    
    def moveDowntest(self):
        self.board=(self.board[3],)+self.board[1:3]+(self.board[0],)+self.board[4:6]
    pass

    #find valid moves or board states
    def find_neighbor(self):
          #hard coded INEFFICIENT
        moveDown0=(self.board[3],)+self.board[1:3]+(self.board[0],)+self.board[4:6]
        moveRight0=(self.board[1],)+(self.board[0],)+self.board[2:6]
        moveDown1=(self.board[0],)+(self.board[4],)+self.board[2:4]+(self.board[1],)+(self.board[5],)
        moveRight1=(self.board[0],)+(self.board[2],)+(self.board[1],)+self.board[3:6]
        moveLeft1=(self.board[0],)+(self.board[2],)+(self.board[1],)+self.board[3:6]
        
        #valid move table
        validMove = {
            0:[moveDown0,moveRight0], #top left corner
            1:[moveDown1,moveRight1,moveLeft1], #top side
            2:[(0,2,0,0,0,0)],#[moveDown,moveLeft], #top right corner
            3:[(0,0,3,0,0,0)],#[moveUp,moveRight], #bottom left corner
            4:[(0,0,0,4,0,0)],#[moveRight,moveUp,moveLeft], #bottom side
            5:[(0,0,0,0,5,0)],#[moveUp,moveLeft], #bottom right corner
        }

        return validMove[self.emptyCell]
        

    #print board state
    def print(self):
        print("board:\n",self.board[0:3],"\n",self.board[3:6])
        print("emptyCell:\n",self.emptyCell)
        return 
    
    #check if it is final state of game
    def is_final_state(self):
        return self.board == (0,1,2,5,4,3)


