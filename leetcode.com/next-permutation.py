#!/bin/python3
# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = i + 1
            while j < len(nums) and nums[i] < nums[j]:
                j += 1
                
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            
        x = i + 1
        y = len(nums) - 1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y -= 1

    def nextPermutation_1(self, nums: list[int]) -> None:
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

if __name__ == "__main__":
    Solution().nextPermutation([5,1,1])
    Solution().nextPermutation([3,2,1])
