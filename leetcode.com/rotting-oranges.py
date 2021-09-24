#!/bin/python3
# https://leetcode.com/problems/rotting-oranges/

empty = 0
fresh = 1
rotten = 2

class Solution:
    def fill(self, grid: list[list[int]], r: int, c: int, days: int) -> bool:
        stable = True

        for delta_r, delta_c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            rr = r + delta_r
            cc = c + delta_c

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]):
                if grid[rr][cc] == fresh:
                    grid[rr][cc] = days + 1
                    stable = False

        return stable

    def orangesRotting(self, grid: list[list[int]]) -> int:
        days = 2
        while True:
            stable = True
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == days:
                        stable = self.fill(grid, r, c, days) and stable

            if stable:
                break
            else:
                days += 1

        max_days = -1
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
                
                max_days = max(max_days, grid[r][c])

        return max_days - 2 if max_days >= 2 else 0

Solution().orangesRotting([[0, 2]])
# Solution().orangesRotting([[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]])        