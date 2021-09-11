#!/bin/python3
# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alphabet = {}
        used_charactes = set()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in alphabet:
                if t[i] in used_charactes:
                    return False
                alphabet[s[i]] = t[i]
                used_charactes.add(t[i])
            elif alphabet[s[i]] != t[i]:
                return False

        return True

Solution().isIsomorphic("badc", "baba")