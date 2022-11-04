#!/bin/python3
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            else:
                if c not in pairs:
                    return False

                if len(stack) == 0:
                    return False

                pair = stack.pop()
                
                if pair != pairs[c]:
                    return False

        return len(stack) == 0