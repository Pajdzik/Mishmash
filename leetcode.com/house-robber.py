#!/bin/python3
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if i + 2 < len(nums):
                nums[i] = max(nums[i + 1], nums[i + 2] + nums[i])
            else:
                nums[i] = max(nums[i], nums[i + 1])

        return nums[0]

    def find_backtracking(self, nums: list[int], index: int, value: int) -> int:
        max_value = value
        for i in range(index + 2, len(nums)):
            new_value = value + self.find(nums, i, value)
            max_value = max(max_value, new_value)

        return max_value + nums[index]

Solution().rob([1, 2])