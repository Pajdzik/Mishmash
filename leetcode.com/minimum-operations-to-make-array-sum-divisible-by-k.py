#!/bin/python3
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        array_sum = sum(nums)
        return array_sum % k


if __name__ == "__main__":
    assert Solution().minOperations([3, 9, 7], 5) == 4
