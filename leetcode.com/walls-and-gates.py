#!/bin/python3
# https://leetcode.com/problems/walls-and-gates/

from typing import Deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        infinity = 2**31 - 1
        queue = Deque()

        for r in range(len(rooms)):
            for c in range(len(rooms[r])):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            r, c, cost = queue.popleft()

            if rooms[r][c] < cost:
                continue

            rooms[r][c] = cost

            for (dr, dc) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if (not 0 <= nr < len(rooms)) or (not 0 <= nc < len(rooms[nr])):
                    continue

                if rooms[nr][nc] != -1:
                    queue.append((nr, nc, cost + 1))

if __name__ == "__main__":
    Solution().wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
