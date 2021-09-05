#!/bin/python3
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = {}
        for l in s:
            if l in ss:
                ss[l] += 1
            else:
                ss[l] = 1

        tt = {}
        for l in t:
            if l in tt:
                tt[l] += 1
            else:
                tt[l] = 1

        for l in ss:
            if l not in tt:
                return False
            if ss[l] != tt[l]:
                return False

        return True

Solution().isAnagram("car", "rat")