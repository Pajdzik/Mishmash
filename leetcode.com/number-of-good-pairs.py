#!/bin/python3
# https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0

        for i, el in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if el == nums[j]:
                    result += 1

        return result
