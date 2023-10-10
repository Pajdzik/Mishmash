#!/bin/python3
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        CLEAR_FLAG = None

        clear_first_row = any([x == 0 for x in matrix[0]])
        clear_first_col = any([matrix[r][0] == 0 for r in range(len(matrix))])

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                if matrix[r][c] == 0:
                    matrix[r][0] = CLEAR_FLAG
                    matrix[0][c] = CLEAR_FLAG

        for c in range(len(matrix[0]) - 1, 0, -1):
            if matrix[0][c] == CLEAR_FLAG:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        for r in range(len(matrix) - 1, 0, -1):
            if matrix[r][0] == CLEAR_FLAG:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0

        if clear_first_col:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        if clear_first_row:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        pass


if __name__ == "__main__":
    def test_and_print_failure(matrix: list[list[int]]):
        result = Solution().setZeroes(matrix)

    test_and_print_failure([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]])

    test_and_print_failure([
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [0, 10, 11, 12],
        [13, 14, 15, 0]])
