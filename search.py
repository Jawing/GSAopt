#!/usr/bin/python
"""define searching functions"""
import copy
import numpy as np
from collections import deque
import gameTable
import heapq
class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        #NOTE:Children:toStore takes more space in memory
        #self.children = children or []
        #store prev move
        self.prev = None
        self.depth = 0
        self.distance = 0
        self.cost = 0
        #Hashkey
        self.id = keyMap(self.game)
    """NOTE:Children
    def getChildren(self):
        self.children = find_neighbour(self)
        return
    """
    #comparison function for heapq
    #comparison order by lower number piece previously moved
    #otherwise return ID
    #HACK recusively compare order by lower number piece
    def __lt__(self, other):
        #BUG could bug if the path is same number and followed to the end
        if self.id == other.id:
            return False
        y,x = self.game.emptyCell[0][0],self.game.emptyCell[1][0]
        yo,xo = other.game.emptyCell[0][0],other.game.emptyCell[1][0]
        if self.parent.game.board[y,x] == other.parent.game.board[yo,xo]:
            while self.parent:
                self = self.parent
                other = other.parent
                return self.__lt__(other)
        else: return self.parent.game.board[y,x] < other.parent.game.board[yo,xo]
        

    #def __lt__(self, other):
     #   return self.id < other.id

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
    #interate through all children in tree
 
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
def explore(game, searchStructure, heuristic):
    #return if start state is final
    if is_final_state(game):
        print("End:")
        return print("Start is final:\n",game.board)
    step = 0 #step countter
    exploredBoard = {} #explored nodes
    #make copy of original, starting game 
    gameCopy = copy.deepcopy(game) 
    #initialize search structure
    queue = searchStructure(Node(gameCopy)) 
    # keep looping until final state is reached
    while queue:
        # pop node
        node = queue.get()
        #NOTE:Debug:show search path
        step += 1
        print("Search Step:", step)
        print_board(node.game)
        # add neighbours of node to queue
        #BFS neighbours = find_neighbourDec(node)
        #DFS neighbours = find_neighbourInc(node)
        neighbours = find_neighbourC(node)

        for neighbour in neighbours:
            #NOTE:Debug:print all neighbours
            #print("neighbour:")
            #print_board(neighbour.game)
            
            #Calculate cost based on heuristic
            neighbour.cost = heuristic(neighbour.game) + neighbour.distance

            # make sure not explore repeated paths
            if  neighbour.id not in exploredBoard:
                # return path if neighbour is goal
                if is_final_state(neighbour.game):
                    pathstep = 0
                    print()
                    for parent in neighbour.rootPath():
                        #NOTE:Debug:show solution path
                        pathstep += 1
                        print("Sol. Backstep:", pathstep)
                        print_board(parent.game)
                    return 
                #add neighbour to queue
                queue.append(neighbour)
        # add node to list of checked nodes
        exploredBoard[node.id] = node
    return print("Error final state not found")


def exploreiter(game, heuristic):
    #return if start state is final
    if is_final_state(game):
        print("End:")
        return print("Start is final:\n",game.board)
    step = 0 #step countter
    exploredBoard = {} #explored nodes
    #make copy of original, starting game 
    gameCopy = copy.deepcopy(game) 
    #initialize search structure
    queue = deque([Node(gameCopy)]) 
    #store the bottom nodes using heapQueue to keep order priority
    #see Node class __lt__ function
    iterQueue = []
    maxDepth = 0

    # keep looping until final state is reached
    while queue:
        # pop node
        node = queue.pop()
        # push current nodes at maxDepth to heap
        while node.depth >= maxDepth: 
            heapq.heappush(iterQueue,(node))
            # if queue not empty pop a node
            if queue: 
                node = queue.pop()
            # if empty increase max depth, push back
            # nodes from heap to stack queue
            else:
                maxDepth += 1
                while iterQueue:
                    queue.appendleft(heapq.heappop(iterQueue))
                node = queue.pop()
                

        #NOTE:Debug:show search path and depth
        step += 1
        print("Search Step:", step)
        print("max depth",maxDepth)
        print("node depth",node.depth)
        print_board(node.game)
        

        # add neighbours of node to queue
        #BFS 
        #neighbours = find_neighbourDec(node)
        #DFS
        neighbours = find_neighbourInc(node)
        #neighbours = find_neighbourC(node)

        for neighbour in neighbours:
            #NOTE:Debug:print all neighbours
            #print("neighbour:")
            #print_board(neighbour.game)
            
            #Calculate cost based on heuristic
            neighbour.cost = heuristic(neighbour.game) + neighbour.distance

            # make sure not explore repeated paths
            if  neighbour.id not in exploredBoard:
                # return path if neighbour is goal
                if is_final_state(neighbour.game):
                    pathstep = 0
                    print()
                    for parent in neighbour.rootPath():
                        #NOTE:Debug:show solution path
                        pathstep += 1
                        print("Sol. Backstep:", pathstep)
                        print_board(parent.game)
                    return 
                #add neighbour to queue
                queue.append(neighbour)
        # add node to list of checked nodes
        exploredBoard[node.id] = node
    return print("depth too shallow final state not found")


#different searching Structure
class SearchQueue:
    def __init__(self,node):
        self.list = deque([node])
    def get(self):
        return self.list.popleft()
    def append(self,node):
        return self.list.append(node)
class SearchStack:
    def __init__(self,node):
        self.list = deque([node])
    def get(self):
        return self.list.pop()
    def append(self,node):
        return self.list.append(node)
class SearchHeap:
    def __init__(self,node):
        self.list = []
        heapq.heappush(self.list, (node.distance,node))
    def get(self):
        return heapq.heappop(self.list)[1]
    def append(self,node):
        return heapq.heappush(self.list, (node.distance,node))

# key mapping for explored nodes
def keyMap(game):
    return tuple(map(tuple,game.board))


#NOTE could return all valid moves as node's children
#DRUL order find neighbour BFS
#LURD order find neighbour DFS
def find_neighbourCC(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        #NOTE Each edge only cost 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    return neighbours

#DRUL order find neighbour DFS
#LURD order find neighbour BFS
def find_neighbourC(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        neighbours.append(newNode)
    return neighbours 

#Order by lower numbered piece Decreasing
def find_neighbourDec(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (moveCost,newNode))
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (moveCost,newNode))
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (moveCost,newNode))
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (moveCost,newNode))
    getList = []
    while neighbours:
        getList.append(heapq.heappop(neighbours)[1])
    return getList 

#Order by lower numbered piece Increasing
def find_neighbourInc(node):
    #optimized by checking prev move
    #valid node list
    neighbours = []
    y,x = node.game.emptyCell[0][0],node.game.emptyCell[1][0]
    if (x > 0) and node.prev != "R":
        newNode = Node(moveLeft(node.game),node)
        newNode.prev = "L"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (-moveCost,newNode))
    if (y > 0) and node.prev != "D":
        newNode = Node(moveUp(node.game),node)
        newNode.prev = "U"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (-moveCost,newNode))
    if (x < (node.game.board.shape[1]-1)) and node.prev != "L":
        newNode = Node(moveRight(node.game),node)
        newNode.prev = "R"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (-moveCost,newNode))
    if (y < (node.game.board.shape[0]-1)) and node.prev != "U":
        newNode = Node(moveDown(node.game),node)
        newNode.prev = "D"
        newNode.depth = node.depth + 1
        newNode.distance = node.distance + 1
        moveCost = newNode.game.board[y][x]
        heapq.heappush(neighbours, (-moveCost,newNode))
    getList = []
    while neighbours:
        getList.append(heapq.heappop(neighbours)[1])
    return getList 

#print board state
def print_board(game):
    print(game.board)
    #print("emptyCell:\n",game.emptyCell,"\n")
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