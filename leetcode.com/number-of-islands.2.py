#!/bin/python3
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def mark_island(si: int, sj: int):
            queue = [(si, sj)]

            while queue:
                i, j = queue.pop()
                if not 0 <= i < len(grid):
                    continue
                if not 0 <= j < len(grid[i]):
                    continue
                if grid[i][j] != "1":
                    continue

                grid[i][j] = "2"
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.append((i + di, j + dj))


        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    mark_island(i, j)
                    number_of_islands += 1

        return number_of_islands