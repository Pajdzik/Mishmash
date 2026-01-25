#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even_sum = sum([nums[r] for r in range(0, len(nums), 2)])
        odd_sum = sum([nums[r] for r in range(1, len(nums), 2)])

        return even_sum - odd_sum


if __name__ == "__main__":
    assert Solution().alternatingSum([1, 3, 5, 7]) == -4
    pass
