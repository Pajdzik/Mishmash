#!/bin/python3
#https://www.hackerrank.com/challenges/castle-on-the-grid

import math
import os
import random
import re
import sys

def find_shortest(grid, queue, goal_x, goal_y):
    visited = []
    grid_size = len(grid)
    min_moves = grid_size * grid_size

    while queue:
        node = queue.pop(0)

        if node[:2] not in visited:
            visited.append(node[:2])

            if node[0] == goal_x and node[1] == goal_y:
                if node[2] < min_moves:
                    min_moves = node[2]
            
            # go left
            x = node[0]
            while x - 1 >= 0 and grid[x - 1][node[1]] != 'X':
                x -= 1

            if x != node[0]:
                queue.append((x, node[1], node[2] + 1))

            # go up
            y = node[1]
            while y - 1 >= 0 and grid[node[0]][y - 1] != 'X':
                y -= 1

            if y != node[1] - 1:
                queue.append((node[0], y, node[2] + 1))

            # go right
            x = node[0]
            while x + 1 < grid_size and grid[x + 1][node[1]] != 'X':
                x += 1
                
            if x != node[0]:
                queue.append((x, node[1], node[2] + 1))

            # go down
            y = node[1]
            while y + 1 < grid_size and grid[node[0]][y + 1] != 'X':
                y += 1

            if y != node[1]:
                queue.append((node[0], y, node[2] + 1))

    return min_moves

def minimumMoves(grid, start_x, start_y, goal_x, goal_y):
    parsed_grid = [[c for c in s] for s in grid]
    return find_shortest(parsed_grid, [(start_x, start_y, 0)], goal_x, goal_y)

if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(str(result) + '\n')
