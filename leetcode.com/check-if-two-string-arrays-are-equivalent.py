#!/bin/python3
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
