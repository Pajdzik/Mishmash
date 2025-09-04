#!/bin/python3
# https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff = abs(x - z) - abs(y - z)
        if diff < 0:
            return 1
        elif diff > 0:
            return 2
        else:
            return 0
