#!/bin/python3
# https://leetcode.com/problems/convert-1d-array-into-2d-array

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        acc = []

        if len(original) != m * n:
            return []

        for i, el in enumerate(original):
            acc.append(el)
            if (i + 1) % n == 0:
                result.append(acc)
                acc = []

        return result
