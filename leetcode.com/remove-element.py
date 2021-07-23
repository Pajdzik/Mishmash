#!/bin/python3
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        delta = 0
        i = 0
        while i + delta < (len(nums)):
            if nums[i + delta] == val:
                while i + delta < len(nums) and nums[i + delta] == val:
                    delta += 1

            if i + delta >= len(nums):
                return i
                
            nums[i] = nums[i + delta]
            i += 1

        return i


Solution().removeElement([0,1,2,2,3,0,4,2], 2)
# Solution().removeElement([3,2,2,3], 3)