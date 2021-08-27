#!/bin/python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            while nums[i] == nums[j]:
                j += 1
                if j == len(nums):
                    return i + 1

            nums[i + 1] = nums[j]
            i += 1
            j += 1

        return i + 1

Solution().removeDuplicates([1, 1])