#!/bin/python3
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])
        left = 0
        right = row_count * col_count - 1

        while left <= right:
            middle = (left + right) // 2
            
            r = middle // col_count
            c = middle % col_count

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False
            
    def searchMatrix_two_binary_searches(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        row = None

        while top <= bottom:
            middle = top + ((bottom - top) // 2)
            if middle < len(matrix) - 1 \
                and target >= matrix[middle][0] \
                and target < matrix[middle + 1][0]:
                    row = middle
                    break
            elif middle == len(matrix) - 1 \
                and target >= matrix[middle][0]:
                    row = middle
                    break
            else:
                if target > matrix[middle][0]:
                    top = middle + 1
                else:
                    bottom = middle - 1

        if row == None:
            return False

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False

Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
Solution().searchMatrix([[1], [3]], 3)