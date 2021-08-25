#!/bin/python3
# https://leetcode.com/problems/spiral-matrix/

east = (0, 1)
south = (1, 0)
west = (0, -1)
north = (-1, 0)

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 1:
            return matrix[0]
        
        visited = []

        len_i = len(matrix)
        len_j = len(matrix[0])

        i = 0
        j = 0
        direction = east

        while len(visited) < len_i * len_j:
            visited.append((i, j))

            dir_i, dir_j = direction
            next_i, next_j = i + dir_i, j + dir_j
            
            if (next_i, next_j) in visited:
                if direction == east:
                    direction = south
                elif direction == south:
                    direction = west
                elif direction == west:
                    direction = north
                elif direction == north:
                    direction = east
            else:
                if i == len_i - 1:
                    if j == 0:
                        direction = north
                    elif j == len_j - 1:
                        direction = west
                elif i == 0 and j == len_j - 1:
                    direction = south

            dir_i, dir_j = direction
            i += dir_i
            j += dir_j
            
        result = [ matrix[i][j] for (i, j) in visited ]
        return result

Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])