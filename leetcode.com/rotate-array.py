#!/bin/python3
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for _ in range(0, k):
            previous_value = nums[0]
            for i in range(1, len(nums)):
                temp = nums[i]
                nums[i] = previous_value
                previous_value = temp

            nums[0] = previous_value

        pass

Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)