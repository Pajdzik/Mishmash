#!/bin/python3
# https://leetcode.com/problems/permutation-difference-between-two-strings/


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - t.find(s[i])) for i in range(len(s)))
