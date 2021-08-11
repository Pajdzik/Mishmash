#!/bin/python3
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
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