#!/usr/bin/python
"""define gameTable object"""

import numpy as np
#import math
#import pickle
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

    #bfs searching algorithm
    def exploreBFS(self):
        
        #if start state is final
        if self.is_final_state():
            print("BFS:")
            return print("Start is final:\n",self.board)
        step = 0 
        queue = deque([[self.board]])
        

        # keep looping until final state is reached
        while queue:
            # initialize path and pop from queue
            path = queue.popleft()
            
            #current board from path
            self.board = path[-1]
            self.boardKey = tuple(map(tuple,self.board))
            self.emptyCell = np.where(self.board == 0)
            
            # debug:show steps and board pathing
            step += 1
            print("step:", step)
            self.print()
            
            # add neighbours of node to queue
            neighbours = self.find_neighbor()
            for neighbour in neighbours:
                # make sure not explore repeated paths
                if  tuple(map(tuple,neighbour)) not in self.exploredBoard:
                    # return path if neighbour is goal
                    if np.array_equal(neighbour,[[0, 1, 2], [5, 4, 3]]):
                        path.append(neighbour)
                        print("BFS:")
                        return print(*path, sep='\n-------\n')
                    #keep track of path
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
            # add node to list of checked nodes
            self.exploredBoard[self.boardKey] = True
        return 

    def exploreDFS(self):
        
        #if start state is final
        if self.is_final_state():
            print("DFS:")
            return print("Start is final:\n",self.board)
        step = 0 
        queue = deque([[self.board]])
        

        # keep looping until final state is reached
        while queue:
            # initialize path and pop from queue
            path = queue.pop()
            
            #current board from path
            self.board = path[-1]
            self.boardKey = tuple(map(tuple,self.board))
            self.emptyCell = np.where(self.board == 0)
            
            # debug:show steps and board pathing
            step += 1
            print("step:", step)
            self.print()
            
            # add neighbours of node to queue
            neighbours = self.find_neighbor()
            for neighbour in neighbours:
                # make sure not explore repeated paths
                if  tuple(map(tuple,neighbour)) not in self.exploredBoard:
                    # return path if neighbour is goal
                    if np.array_equal(neighbour,[[0, 1, 2], [5, 4, 3]]):
                        path.append(neighbour)
                        print("DFS:")
                        return print(*path, sep='\n-------\n')
                    #keep track of path
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
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


