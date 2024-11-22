#!/bin/python3
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        sorted_nums = sorted(nums)
        s = 0
        e = len(nums) - 1

        while s < e:
            sm = sorted_nums[s] + sorted_nums[e]
            if sm < target:
                result += e - s
                s += 1
            else:
                e -= 1

        return result

    def countPairs_loops(self, nums: List[int], target: int) -> int:
        result = 0
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                if nums[i] + nums[j] < target:
                    result += 1

        return result
