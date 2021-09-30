#!/bin/python3
# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        
        k = n - 1
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1

        if k >= 0:
            l = n
            while l > k and nums[k] >= nums[l]:
                l -= 1

            nums[k], nums[l] = nums[l], nums[k]

        k += 1
        while k < n:
            nums[k], nums[n] = nums[n], nums[k]
            k += 1
            n -= 1

Solution().nextPermutation([3,2,1])
