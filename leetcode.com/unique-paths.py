#!/bin/python3
# https://leetcode.com/problems/unique-paths/

class Solution:
    def backtrack(self, m: int, n: int, curr_m: int, curr_n: int, count: int) -> int:
        if not 0 <= curr_m < m:
            return 0

        if not 0 <= curr_n < n:
            return 0

        if curr_m == m - 1 and curr_n == n - 1:
            return 1
        
        return self.backtrack(m, n, curr_m + 1, curr_n, count + 1) \
            + self.backtrack(m, n, curr_m, curr_n + 1, count + 1)

    def uniquePaths(self, m: int, n: int) -> int:
        memory = [ [ 1 for _ in range(n) ] for _ in range(m) ]

        for row in range(1, m):
            for column in range(1, n):
                memory[row][column] = memory[row - 1][column] + memory[row][column - 1]

        return memory[-1][-1]
        
if __name__ == "__main__":
    Solution().uniquePaths(3, 7)