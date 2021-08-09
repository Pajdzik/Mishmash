#!/bin/python3
# https://leetcode.com/problems/single-number/

from typing import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res

    def singleNumber_hashmap(self, nums: list[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for c in counter:
            if counter[c] == 1:
                return c