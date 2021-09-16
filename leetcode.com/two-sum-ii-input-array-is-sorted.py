#!/bin/python3
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] > target:
            right -= 1

        while numbers[left] + numbers[right] < target:
            left += 1

        return [left + 1, right + 1]

Solution().twoSum([2,7,11,15], 9)