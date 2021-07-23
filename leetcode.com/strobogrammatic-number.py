#!/bin/python3
# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        for i in range(0, len(num) // 2 + 1):
            other_letter = num[len(num) - i  - 1]
            if num[i] not in strobogrammatic_map:
                return False
            if other_letter not in strobogrammatic_map:
                return False
            if num[i] != strobogrammatic_map[other_letter]:
               return False

        return True

Solution().isStrobogrammatic("659")