#!/bin/python3
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in cache:
                return [ cache[diff], i ]

            cache[num] = i

    def twoSum_bruteforce(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

Solution().twoSum([3,2,4], 6)