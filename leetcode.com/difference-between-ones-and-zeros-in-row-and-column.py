#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        nr = len(grid)
        nc = len(grid[0])

        cols = [[0] * nc, [0] * nc]
        rows = [[0] * nr, [0] * nr]

        for r in range(nr):
            for c in range(nc):
                el = grid[r][c]
                cols[el][c] += 1
                rows[el][r] += 1

        for i in range(nr):
            for j in range(nc):
                grid[i][j] = cols[1][j] + rows[1][i] - cols[0][j] - rows[0][i]

        return grid


if __name__ == "__main__":
    assert Solution().onesMinusZeros([[1, 1, 1], [1, 1, 1]]) == [[5, 5, 5], [5, 5, 5]]
    assert Solution().onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]) == [
        [0, 0, 4],
        [0, 0, 4],
        [-2, -2, 2],
    ]
