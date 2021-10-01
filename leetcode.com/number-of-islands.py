#!/bin/python3
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def visit_island(self, grid: list[list[str]], start_r: int, start_c: int) -> set:
        queue = [ (start_r, start_c) ]
        island = set()

        while queue:
            r, c = queue.pop()
            if (r, c) in island or grid[r][c] != '1':
                continue
            
            island.add((r, c))

            for (delta_r, delta_c) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= r + delta_r < len(grid) and 0 <= c + delta_c < len(grid[0]):
                    queue.append((r + delta_r, c + delta_c))

        return island
                    

    def numIslands(self, grid: list[list[str]]) -> int:
        visited = set()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in visited and grid[r][c] == '1':
                    island = self.visit_island(grid, r, c,)
                    visited.update(island)
                    count += 1

        return count

Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])