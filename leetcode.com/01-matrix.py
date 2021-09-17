#!/bin/python3
# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        output = [ [None for _ in range(len(mat[0]))] for _ in range(len(mat))]
        filled = 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    output[r][c] = 0
                    filled += 1

        dist = 0
        while filled < len(mat) * len(mat[0]):
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    if output[r][c] == dist:
                        for (delta_r, delta_c) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            if 0 <= r + delta_r < len(mat) \
                                and 0 <= c + delta_c < len(mat[0]) \
                                and output[r + delta_r][c + delta_c] == None:
                                    output[r + delta_r][c + delta_c] = dist + 1
                                    filled += 1

            dist += 1

        return output

mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
Solution().updateMatrix(mat)