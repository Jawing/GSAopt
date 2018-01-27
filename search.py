#!/usr/bin/python
"""define searching functions"""
import copy
import numpy as np
from collections import deque
import gameTable
import heapq
class Node:
    def __init__(self, game, parent=None, children=None):
        self.game = game
        self.parent = parent
        #children not implemented in methods below
        #self.children = children or []
        #store prev move
        self.prev = None
        #TODO implement depth 
        self.depth = 0.
        #TODO implement cost function
        #cost
        self.cost = manhattanCost(self.game)
        #Hashkey
        self.id = keyMap(self.game)
        
        #comparison function for heapq after depth
        #TODO currenly only using id, future use cost?
        def __lt__(self, other):
            return self.id < other.id
        def __eq__(self, other):
            return self.id == other.id

    """Currently not used
    def add_child(self, game):
        new_child = Tree(game, parent=self)
        self.children.append(new_child)
        return new_child

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.game)
        return '{game} [{children}]'.format(game=self.game, children=', '.join(map(str, self.children)))
    
    #interate through all children
    def getChild(self):
        yield self
        for child in self.children:
            for node in child:
                yield node
    """
    
    #parentPath returns everything to original
    def rootPath(self):
        yield self
        while self.parent != None:
            self = self.parent
            yield self

#Searching algorithm
def explore(game, searchStructure):
    #if start state is final
    if is_final_state(game):
        print("End:")
        return print("Start is final:\n",game.board)
    step = 0 
    #explored nodes
    exploredBoard = {} 
    #make copy of original, starting game
    gameCopy = copy.deepcopy(game)
    #initialize search structure
    queue = searchStructure(Node(gameCopy))
    # keep looping until final state is reached
    while queue:
        # initialize path and apply bfs or dfs to queue
        node = queue.get()
        #print(manhattanCost(node.game.board))
        #debug:show steps and board pathing
        step += 1
        print("step:", step)
        print_board(node.game)
        # add neighbours of node to queue
        neighbours = find_neighbor(node)
        depth = 0
        for neighbour in neighbours:
            #print("neighbour:")
            #print_board(neighbour.game)
            # make sure not explore repeated paths
            if  neighbour.id not in exploredBoard:
                # return path if neighbour is goal
                if is_final_state(neighbour.game):
                    pathstep = 0
                    #print("backstep:", pathstep)
                    #print_board(neighbour.game)
                    for parent in neighbour.rootPath():
                        pathstep += 1
                        print("backstep:", pathstep)
                        print_board(parent.game)
                    return 
                
                
                #workaround node comparison
                depth += 0.1
                neighbour.depth += depth
                
                #add neighbour to queue
                queue.append(neighbour)


        # add node to list of checked nodes
        exploredBoard[node.id] = node
    return 

#different searching Structure
class BFS:
    def __init__(self,node):
        self.list = deque([node])
    def get(self):
        return self.list.popleft()
    def append(self,node):
        return self.list.append(node)
class DFS:
    def __init__(self,node):
        self.list = deque([node])
    def get(self):
        return self.list.pop()
    def append(self,node):
        return self.list.append(node)
class BinaryHeap:
    def __init__(self,node):
        self.list = []
        heapq.heappush(self.list, (node.depth,node))
    def get(self):
        return heapq.heappop(self.list)[1]
    def append(self,node):
        #TODO bugged node comparison!!!! 
        return heapq.heappush(self.list, (node.depth,node))

# key mapping for explored nodes
def keyMap(game):
    return tuple(map(tuple,game.board))
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

#return all valid moves as node's children
#Could link to parent as child
#Counter Clockwise find neighbor
def find_neighborCC(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    return neighbours

#Clockwise find neighbor
def find_neighbor(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        #node.children.append(newNode)
        neighbours.append(newNode)
    return neighbours 

#print board state
def print_board(game):
    print("board:\n",game.board)
    print("emptyCell:\n",game.emptyCell,"\n")
    return 

#check if it is final state of game
def is_final_state(game):
    return np.array_equal(game.board,game.goal)

def moveDown(game):
    gameCopy = copy.deepcopy(game)
    y,x = gameCopy.emptyCell[0][0],gameCopy.emptyCell[1][0]
    gameCopy.board[y,x],gameCopy.board[y+1,x] = gameCopy.board[y+1,x],gameCopy.board[y,x]
    gameCopy.emptyCell[0][0] +=1
    return gameCopy
def moveRight(game):
    gameCopy = copy.deepcopy(game)
    y,x = gameCopy.emptyCell[0][0],gameCopy.emptyCell[1][0]
    gameCopy.board[y,x],gameCopy.board[y,x+1] = gameCopy.board[y,x+1],gameCopy.board[y,x]
    gameCopy.emptyCell[1][0] +=1
    return gameCopy
def moveLeft(game):
    gameCopy = copy.deepcopy(game)
    y,x = gameCopy.emptyCell[0][0],gameCopy.emptyCell[1][0]
    gameCopy.board[y,x],gameCopy.board[y,x-1] = gameCopy.board[y,x-1],gameCopy.board[y,x]
    gameCopy.emptyCell[1][0] -=1
    return gameCopy
def moveUp(game):
    gameCopy = copy.deepcopy(game)
    y,x = gameCopy.emptyCell[0][0],gameCopy.emptyCell[1][0]
    gameCopy.board[y,x],gameCopy.board[y-1,x] = gameCopy.board[y-1,x],gameCopy.board[y,x]
    gameCopy.emptyCell[0][0] -=1
    return gameCopy