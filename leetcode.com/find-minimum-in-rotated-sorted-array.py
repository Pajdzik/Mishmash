#!/bin/python3
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            middle = (l + r) // 2
            
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        return nums[l]

Solution().findMin([4,5,6,7,0,1,2])