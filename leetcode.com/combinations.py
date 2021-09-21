#!/bin/python3
# https://leetcode.com/problems/combinations/

class Solution:
    def backtrack(self, first: int, n: int, k: int, result: list[int], results: list[list[int]]) -> None:
        if k == len(result):
            results.append(result[:])
            return

        for i in range(first, n + 1):
            result.append(i)
            self.backtrack(i + 1, n, k, result, results)
            result.pop()
        
    def combine(self, n: int, k: int) -> list[list[int]]:
        results = []
        self.backtrack(1, n, k, [], results)
        return results

r = Solution().combine(4, 2)
print(r)