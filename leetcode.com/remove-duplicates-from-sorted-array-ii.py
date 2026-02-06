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
        to_insert = 2
        current = 2

        while current < len(nums):
            if nums[to_insert - 2] != nums[current]:  # at most two elements in a row
                nums[to_insert] = nums[current]
                to_insert += 1

            current += 1

        return to_insert


if __name__ == "__main__":

    def test(expected, nums):
        sol = Solution()
        result = sol.removeDuplicates(nums)
        assert nums[:result] == expected, (
            f"Expected {expected}, but got {nums[:result]}"
        )

    test([1, 1], [1, 1, 1])
    test([1, 1, 2, 2, 3], [1, 1, 1, 2, 3, 4])
