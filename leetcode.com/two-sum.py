#!/bin/python3
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        
        for i, el in enumerate(nums):
            to_find = target - el
            
            if to_find in map:
                return [map[to_find], i]
            else:
                map[el] = i

        return []

    def twoSum_bruteforce(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

Solution().twoSum([3,2,4], 6)