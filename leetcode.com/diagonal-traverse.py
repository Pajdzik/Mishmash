#!/bin/python3
# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        result = []

        max_c = len(mat[0])
        max_r = len(mat)

        # (r, c)

        up_right = (-1, 1)
        down_left = (1, -1)
        
        dir = up_right

        c = 0
        r = 0

        while c != max_c - 1 or r != max_r - 1:
            result.append(mat[r][c])

            if dir == up_right and (r == 0 or c == max_c - 1):
                dir = down_left
                if c + 1 < max_c:
                    c += 1
                else:
                    r += 1
            elif dir == down_left and (c == 0 or r == max_r - 1):
                dir = up_right
                if r + 1 < max_r:
                    r += 1
                else:
                    c += 1
            else:
                (dir_r, dir_c) = dir
                r += dir_r
                c += dir_c

        result.append(mat[r][c])

        return result

Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])