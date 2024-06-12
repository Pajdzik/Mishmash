#!/bin/python3
# https://leetcode.com/problems/sort-colors/

from collections import Counter


class Solution:

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)

        i = 0
        for color in [0, 1, 2]:
            count = c[color]
            for _ in range(count):
                nums[i] = color
                i += 1

    def sortColors_2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        color = 0
        for i in range(len(nums)):
            while count[color] <= 0:
                color += 1

            nums[i] = color
            count[color] -= 1


nums = [2]
Solution().sortColors(nums)
pass
