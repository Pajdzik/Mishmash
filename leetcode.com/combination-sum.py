#!/bin/python3
# https://leetcode.com/problems/combination-sum/

class Solution:
    def backtrack(self, candidates: list[int], target: int, combination: list[int], sum: int, results: list[list[int]]) -> None:
        if sum > target:
            return

        if sum == target:
            sorted_combination = sorted(combination)
            if sorted_combination not in results:
                results.append(sorted_combination)
            return

        for num in candidates:
            self.backtrack(candidates, target, combination + [num], sum + num, results)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        self.backtrack(candidates, target, [], 0, results)
        return results

if __name__ == "__main__":
    subsets = Solution().combinationSum([1, 2, 3], 6)