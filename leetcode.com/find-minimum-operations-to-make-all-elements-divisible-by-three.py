#!/bin/python3
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(min(num % 3, 3 - (num % 3)) for num in nums)
