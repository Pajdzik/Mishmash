#!/bin/python3
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
            
        result = [ None for _ in range(len(nums)) ]
        for i in range(len(nums)):
            pos = len(nums) - i - 1
            if abs(nums[left]) < abs(nums[right]):
                result[pos] = nums[right] * nums[right]
                right -= 1
            else:
                result[pos] = nums[left] * nums[left]
                left += 1

        return result

Solution().sortedSquares(
[-4,-1,0,3,10])
