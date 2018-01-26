#!/usr/bin/python
"""define searching functions"""
import copy
import numpy as np
from collections import deque
import gameTable

class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        self.children = []

#bfs searching algorithm
def exploreBFS(game):
    #if start state is final
    if is_final_state(game):
        print("BFS:")
        return print("Start is final:\n",game.board)
    step = 0 
    #explored board for the object instance
    exploredBoard = {} 
    #make copy of original
    gameCopy = gameTable.Board(game.board)
    queue = deque([[gameCopy.board]])
    
    # keep looping until final state is reached
    while queue:
        # initialize path and pop from queue
        path = queue.popleft()
        
        #current board from path
        gameCopy.board = path[-1]
        boardKey = tuple(map(tuple,gameCopy.board))
        gameCopy.emptyCell = np.where(gameCopy.board == 0)
        
        #TODO for dfs and bfs
        print(manhattanCost(gameCopy))
        print(naiveCost(gameCopy))

        # debug:show steps and board pathing
        step += 1
        print("step:", step)
        print_board(gameCopy)
        
        # add neighbours of node to queue
        neighbours = find_neighbor(gameCopy)
        for neighbour in neighbours:
            # make sure not explore repeated paths
            if  tuple(map(tuple,neighbour)) not in exploredBoard:
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
        exploredBoard[boardKey] = True
    return 
def exploreDFS(game):
    #if start state is final
    if is_final_state(game):
        print("DFS:")
        return print("Start is final:\n",game.board)
    step = 0 
    #explored board for the object instance
    exploredBoard = {}
    #make copy of original
    gameCopy = copy.copy(game)   
    queue = deque([[gameCopy.board]])
    
    # keep looping until final state is reached
    while queue:
        # initialize path and pop from queue
        path = queue.pop()
        
        #current board from path
        gameCopy.board = path[-1]
        boardKey = tuple(map(tuple,gameCopy.board))
        gameCopy.emptyCell = np.where(gameCopy.board == 0)
        
        # debug:show steps and board pathing
        step += 1
        print("step:", step)
        print_board(gameCopy)
        
        # add neighbours of node to queue
        neighbours = find_neighbor(gameCopy)
        for neighbour in neighbours:
            # make sure not explore repeated paths
            if  tuple(map(tuple,neighbour)) not in exploredBoard:
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
        exploredBoard[boardKey] = True
    return 

#cost heuristic +x+y distance away from location
def manhattanCost(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            xf, yf = game.goalLocation[game.board[y,x]]
            cost += abs(xf - x) + abs(yf - y)
    return cost

#cost heuristic +1 for wrong tile location
def naiveCost(game):
    cost = 0
    for y in range(game.board.shape[0]):
        for x in range(game.board.shape[1]):
            if game.goalLocation[game.board[y,x]] != (x, y):
                cost += 1
    return cost


#find valid moves or board states
def find_neighbor(game):
    #TODO can optimize by saving previous move!!!(game,path,heuristic)
    #valid move table
    x,y=game.emptyCell
    def moveDown():
        board = np.copy(game.board)
        board[x,y],board[x+1,y] = board[x+1,y],board[x,y]
        return board
    def moveRight():
        board = np.copy(game.board)
        board[x,y],board[x,y+1] = board[x,y+1],board[x,y]
        return board
    def moveLeft():
        board = np.copy(game.board)
        board[x,y],board[x,y-1] = board[x,y-1],board[x,y]
        return board
    def moveUp():
        board = np.copy(game.board)
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
def print_board(game):
    print("board:\n",game.board)
    print("emptyCell:\n",game.emptyCell,"\n")
    return 

#check if it is final state of game
def is_final_state(game):
    return np.array_equal(game.board,game.goal)
