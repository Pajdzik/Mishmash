#!/bin/python3
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        delta = 0
        while i + delta < len(nums):
            while i + delta < len(nums) and nums[i + delta] == 0:
                delta += 1

            if i + delta >= len(nums):
                break

            nums[i] = nums[i + delta]
            i += 1
        
        for i in range(i, len(nums)):
            nums[i] = 0

array = [2]
Solution().moveZeroes(array)
print(array)