#!/bin/python3
# https://leetcode.com/problems/single-number-ii/

from typing import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for c in counter:
            if counter[c] == 1:
                return c