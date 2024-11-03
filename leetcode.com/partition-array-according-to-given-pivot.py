#!/bin/python3
# https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        pivots = []
        higher = []

        for num in nums:
            if num < pivot:
                lower.append(num)
            elif num > pivot:
                higher.append(num)
            else:
                pivots.append(num)

        return lower + pivots + higher
