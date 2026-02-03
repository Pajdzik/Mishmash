#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional

"""
Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output:       [[8,2,3],[9,6,7],[4,5,1]]
"""


class Solution:
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:
        def sort_diagonal(row: int, col: int) -> None:
            diagonal = []

            i, j = row, col
            while i < len(grid) and j < len(grid[0]):
                diagonal.append(grid[i][j])
                i += 1
                j += 1

            diagonal.sort()

            i, j = row, col
            for d in range(len(diagonal)):
                grid[i + d][j + d] = diagonal[d]

        for i in range(len(grid)):
            sort_diagonal(i, 0)

        for j in range(1, len(grid[0])):
            sort_diagonal(0, j)

        return grid


if __name__ == "__main__":
    assert Solution().diagonalSort([[1, 7, 3], [9, 8, 2], [4, 5, 6]]) == [
        [8, 2, 3],
        [9, 6, 7],
        [4, 5, 1],
    ]
