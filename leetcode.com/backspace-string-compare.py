#!/bin/python3
# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for c in s:
            if c == "#":
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(c)

        stack_t = []
        for c in t:
            if c == "#":
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(c)

        if len(stack_s) != len(stack_t):
            return False
        
        for i in range(len(stack_s)):
            if stack_s[i] != stack_t[i]:
                return False

        return True

Solution().backspaceCompare("y#fo##f", "y#f#o##f")