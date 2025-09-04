#!/bin/python3
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses_old(self, s: str) -> int:
        if len(s) < 2:
            return 0

        max_length = 0
        length = [ None ] * len(s)
        length[0] = 0

        for i in range(1, len(s)):
            c = s[i]
            
            if c == ')':
                if s[i - 1] == '(':
                    length[i] = (length[i - 2] if i > 1 else 0) + 2
                else: # ')'
                    matching = i - length[i - 1] - 1
                    if matching >= 0 and s[matching] == '(':
                        length[i] = length[i - 1] + (length[matching - 1] if matching > 0 else 0) + 2
                    else:
                        length[i] = 0
            else:
                length[i] = 0
            
            max_length = max(max_length, length[i])

        return max_length

    def longestValidParentheses_brute_force(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            length = 0
            stack = []

            if s[i] == ')':
                continue

            for j in range(i, len(s)):
                if s[j] == '(':
                    stack.append(j)
                    length += 1
                else:
                    if len(stack) == 0:
                        break
                    else:
                        stack.pop()
                        length += 1

            if len(stack) > 0:
                length = stack.pop(0) - i
            if length > max_length:
                max_length = length

        return max_length

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if len(stack) > 0:
                    _ = stack.pop()
                    if len(stack) == 0:
                        stack.append(i)
                    else:
                        max_length = max(i - stack[-1], max_length)

        return max_length


if __name__ == "__main__":
    assert 4 == Solution().longestValidParentheses("(()()")
    assert 2 == Solution().longestValidParentheses("(()")
    assert 6 == Solution().longestValidParentheses("()(())")
