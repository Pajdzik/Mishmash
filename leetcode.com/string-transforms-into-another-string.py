#!/bin/python3
# https://leetcode.com/problems/string-transforms-into-another-string/

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        elif str1 == str2:
            return True

        conversion_map = {}

        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]

            if c1 in conversion_map and conversion_map[c1] != c2:
                return False

            conversion_map[c1] = c2

        return len(set(str2)) < 26

if __name__ == "__main__":
    assert(Solution().canConvert("ab", "ba"))
    assert(not Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))