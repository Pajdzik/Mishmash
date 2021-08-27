#!/bin/python3
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            if s[i].isalnum():
                break
            i -= 1

        length = 0
        while i >= 0:
            if s[i].isalnum():
                length += 1
            else:
                break
            i -= 1

        return length

Solution().lengthOfLastWord("   fly me   to   the moon  ")