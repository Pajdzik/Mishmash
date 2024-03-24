#!/bin/python3
# https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ""
        for i in range(0, len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if max_digit < num[i]:
                    max_digit = num[i]

        return max_digit * 3
