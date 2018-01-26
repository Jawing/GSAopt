#!/usr/bin/python
"""define searching functions"""
import copy
import numpy as np
from collections import deque

class Node:
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = children or []
        #store prev move
        self.prev = None
        
    def add_child(self, data):
        new_child = Tree(data, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))

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
    gameCopy = copy.copy(game)
    #initialize start queue
    queue = deque([gameCopy])
    
    # keep looping until final state is reached
    while queue:
        # initialize path and pop from queue
        node = Node(queue.popleft())
        #current board from path
        boardKey = keyMap(node.game.board)
        cost = manhattanCost(node.game.board)

        # debug:show steps and board pathing
        step += 1
        print("step:", step)
        print_board(node.game)
        
        # add neighbours of node to queue
        neighbours = find_neighbor(node)
        for neighbour in neighbours:
            # make sure not explore repeated paths
            if  keyMap(neighbour) not in exploredBoard:
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
        boardKey = keyMap(gameCopy.board)
        gameCopy.emptyCell = np.where(gameCopy.board == 0)
        
        # debug:show steps and board pathing
        step += 1
        print("step:", step)
        print_board(gameCopy)
        
        # add neighbours of node to queue
        neighbours = find_neighbor(gameCopy)
        for neighbour in neighbours:
            # make sure not explore repeated paths
            if  keyMap(neighbour) not in exploredBoard:
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

# key mapping for explored nodes
def keyMap(board):
    return tuple(map(tuple,board))
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
def find_neighbor(node):
    #TODO can optimize by saving previous move!!!(game,path,heuristic)
    #valid move table
    #TODO change x y variables
    x,y=node.game.emptyCell
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
