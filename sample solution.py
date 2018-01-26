#!/usr/bin/python

import sys
import copy


class Board:
    def __init__(self, matrix, whitepos=None):
        self.matrix = matrix
        self.whitepos = whitepos
        if not whitepos:
            for y in range(3):
                for x in range(3):
                    if board[y][x] == 0:
                        self.whitepos = (x, y)


def is_final_state(board):
    final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    for y in range(3):
        for x in range(3):
            if board.matrix[y][x] != final[y][x]:
                return False
    return True


def get_whitepos(board):
    return board.whitepos


def move(board, x, y, dx, dy):
    b = copy.deepcopy(board.matrix)
    b[y][x] = b[y + dy][x + dx]
    b[y + dy][x + dx] = 0
    return Board(b, (x + dx, y + dy))


def manhattan_heur(board):
    finalpos = [(1, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2),
                (0, 1)]
    cost = 0
    for y in range(3):
        for x in range(3):
            t = board.matrix[y][x]
            xf, yf = finalpos[t]
            cost += abs(xf - x) + abs(yf - y)
    return cost


def wrongplace_heur(board):
    finalpos = [(1, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2),
                (0, 1)]
    cost = 0
    for y in range(3):
        for x in range(3):
            t = board.matrix[y][x]
            if finalpos[t] != (x, y):
                cost += 1
    return cost


def heuristic(board):
    return manhattan_heur(board)


class Node:
    def __init__(self, board, parent):
        self.state = board
        self.parent = parent
        if not parent:
            self.g = 0
        else:
            self.g = parent.g + 1
        self.h = heuristic(board)

    def test_goal(self):
        return is_final_state(self.state)

    def expand(self):
        children = []
        b = self.state
        x, y = get_whitepos(b)
        if x > 0:
            children.append(Node(move(b, x, y, -1, 0), self))
        if x < 2:
            children.append(Node(move(b, x, y, +1, 0), self))
        if y > 0:
            children.append(Node(move(b, x, y, 0, -1), self))
        if y < 2:
            children.append(Node(move(b, x, y, 0, +1), self))
        return children


class Solution:
    def __init__(self, node, mem_needed, steps):
        self.node = node
        self.mem_needed = mem_needed
        self.iterations = steps

    def inc(self, other):
        self.node = other.node
        self.mem_needed = max(self.mem_needed, other.mem_needed)
        self.iterations += other.iterations


def search(board, queue_fn, queue_arg=None):
    max_nodes = 1
    steps = 0
    nodes = [Node(Board(board), None)]
    prev = []
    depth = 0
    while nodes:
        node = nodes.pop(0)

        if node.g > depth:
            depth = node.g
            print(depth)

        if node in prev:
            continue
        prev.append(node)

        if node.test_goal():
            return Solution(node, max_nodes, steps)
        new_nodes = node.expand()
        nodes = queue_fn(nodes, new_nodes, queue_arg)

        max_nodes = max(max_nodes, len(nodes))
        steps += 1
    return Solution(None, max_nodes, steps)


def fifo_queue(nodes, new_nodes, _):
    nodes.extend(new_nodes)
    return nodes


def bl_search(board):
    return search(board, fifo_queue)


def lifo_queue(nodes, new_nodes, _):
    new_nodes.extend(nodes)
    return new_nodes


def dfs_search(board):
    return search(board, lifo_queue)


def bpl_queue(nodes, new_nodes, max_depth):
    def f(n):
        return n.g <= max_depth

    new_nodes = filter(f, new_nodes)
    new_nodes.extend(nodes)
    return new_nodes


def bpi_search(board):
    solution = Solution(None, 0, 0)
    for max_depth in range(0, sys.maxint):
        sol = search(board, bpl_queue, max_depth)
        solution.inc(sol)
        if solution.node:
            return solution


def sort_queue(nodes, new_nodes, cmp):
    nodes.extend(new_nodes)
    nodes.sort(cmp)
    return nodes


def guloso2_search(board):
    def cmp(n1, n2):
        return n1.h - n2.h

    return search(board, sort_queue, cmp)


def astar_search(board):
    def cmp(n1, n2):
        return (n1.g + n1.h) - (n2.g + n2.h)

    return search(board, sort_queue, cmp)


def print_solution(search, sol):
    print
    print("*", search)
    node = sol.node
    if node:
        print("moves:", node.g)
        while node:
            print("\t", node.state.matrix)
            node = node.parent
    else:
        print("no solution found")
    print("nodes needed:", sol.mem_needed)
    print("iterations:  ", sol.iterations)


board = [[6, 5, 7], [2, 0, 1], [8, 4, 3]]

print_solution("bl", bl_search(board))
print_solution("dfs", dfs_search(board))
print_solution("bpi", bpi_search(board))
print_solution("guloso2", guloso2_search(board))
print_solution("astar", astar_search(board))