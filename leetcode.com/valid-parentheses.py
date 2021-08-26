#!/bin/python3
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in {'{', '(', '['}:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if (c == '}' and p != '{') \
                    or (c == ']' and p != '[') \
                    or (c == ')' and p != '('):
                    return False

        return len(stack) == 0