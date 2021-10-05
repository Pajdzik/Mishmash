#!/bin/python3
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = self.subsets_cascading(nums)
        return results

    def subsets_cascading(self, nums: list[int]) -> list[list[int]]:
        index = 0
        results = [[]]

        while index < len(nums):
            current_len = len(results)
            for i in range(current_len):
                results.append(results[i] + [nums[index]])

            index += 1

        return results

    def subsets_recursive(self, nums: list[int], index: int, subset: list[int], results: list[list[int]]) -> None:
        if index >= len(nums):
            return

        subset.append(nums[index])
        results.append(subset[:])
        self.subsets_recursive(nums, index + 1, subset, results)
        subset.pop()
        self.subsets_recursive(nums, index + 1, subset, results)

    
    def subsets_binarymask(self, nums: list[int]) -> list[list[int]]:
        count_of_subsets = 2**len(nums)
        subsets = []

        for i in range(count_of_subsets):
            subset = []

            for b in range(len(nums)):
                if (1 << b) & i:
                    subset.append(nums[b])

            subsets.append(subset)
        
        return subsets

subsets = Solution().subsets([1, 2, 3])