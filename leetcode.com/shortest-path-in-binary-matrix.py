#!/bin/python3
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid) - 1
        visited = set()
        queue = [ (0, 0, 0) ]

        while queue:
            r, c, length = queue.pop(0)

            if not 0 <= r < len(grid):
                continue
            if not 0 <= c < len(grid):
                continue
            if grid[r][c] == 1:
                continue
            if r == n and c == n:
                return length + 1
            if (r, c) in visited:
                continue

            visited.add((r, c))

            for delta_r, delta_c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                queue.append((r + delta_r, c + delta_c, length + 1))

        return -1

if __name__ == "__main__":
    Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]])