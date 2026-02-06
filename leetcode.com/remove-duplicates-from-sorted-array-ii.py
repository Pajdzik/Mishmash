#!/bin/python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

""" 
       i  c
[1, 1, 1, 2, 2, 3]
          i  c
[1, 1, 2, 2, 2, 3]
             i  c
[1, 1, 2, 2, 2, 3]

[1, 1, 2, 2, 3, 3]

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 2
        for i in range(2, len(nums)):
            if nums[current - 2] != nums[i]:
                nums[current] = nums[i]
                current += 1

        return current


if __name__ == "__main__":

    def test(expected, nums):
        sol = Solution()
        result = sol.removeDuplicates(nums)
        assert nums[:result] == expected, (
            f"Expected {expected}, but got {nums[:result]}"
        )

    test([1, 1], [1, 1, 1])
    test([1, 1, 2, 2, 3], [1, 1, 1, 2, 3, 4])
