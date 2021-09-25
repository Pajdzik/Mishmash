#!/bin/python3
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) == 0 or len(mat) * len(mat[0]) != r * c:
            return mat
            
        output = [ ]

        x = y = 0
        for i in range(r):
            output.append([])

            for j in range(c):
                output[i].append(mat[x][y])

                y += 1
                if y == len(mat[x]):
                    x += 1
                    y = 0
                    if x == len(mat):
                        return output

Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)