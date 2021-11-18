#!/bin/python3
# https://leetcode.com/problems/minimum-path-sum/

from collections import deque

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        costs = [ float("inf") for _ in range(len(grid[0])) ]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r == 0 and c == 0:
                    costs[c] = grid[0][0]
                    continue

                cost = grid[r][c]

                path_cost = costs[c] + cost
                if 0 <= c - 1:
                    path_cost = min(path_cost, costs[c - 1] + cost)

                costs[c] = path_cost

        return costs[-1]

    def minPathSum_front_dp(self, grid: list[list[int]]) -> int:
        costs = [ [ float("inf") for _ in range(len(grid[i])) ] for i in range(len(grid)) ]

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if r == 0 and c == 0:
                    costs[r][c] = grid[r][c]
                    continue

                cost = grid[r][c]
                path_cost = float("inf")

                if 0 <= r - 1:
                    path_cost = min(path_cost, costs[r - 1][c] + cost)
                if 0 <= c - 1:
                    path_cost = min(path_cost, costs[r][c - 1] + cost)

                costs[r][c] = path_cost

        return costs[-1][-1]

    def minPathSum_reverse_dp(self, grid: list[list[int]]) -> int:
        costs = [ [ float("inf") for _ in range(len(grid[i])) ] for i in range(len(grid)) ]

        for r in range(len(grid) - 1, -1, -1):
            for c in range(len(grid[r]) - 1, -1, -1):
                if r == len(grid) - 1 and c == len(grid[r]) - 1:
                    costs[r][c] = grid[r][c]
                    continue
                
                cost = grid[r][c]
                path_cost = float("inf")
                if 0 <= r + 1 < len(grid):
                    path_cost = min(path_cost, costs[r + 1][c] + cost)
                if 0 <= c + 1 < len(grid[r]):
                    path_cost = min(path_cost, costs[r][c + 1] + cost)

                costs[r][c] = path_cost

        return costs[0][0]

    def minPathSum_tle(self, grid: list[list[int]]) -> int:
        queue = deque([(0, 0, 0)])

        costs = [ [ float("inf") for _ in range(len(grid[i])) ] for i in range(len(grid)) ]

        while queue:
            r, c, cost = queue.popleft()
            
            new_cost = cost + grid[r][c]
            if new_cost >= costs[r][c]:
                continue

            costs[r][c] = new_cost

            for dr, dc in [(1, 0), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < len(grid)) and  (0 <= nc < len(grid[nr])):
                    if costs[nr][nc] >= costs[r][c] + grid[nr][nc]:
                        queue.append((nr, nc, costs[r][c]))

        return costs[-1][-1]

if __name__ == "__main__":
    assert(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)
    assert(Solution().minPathSum([[1,2],[1,1]]) == 3)
