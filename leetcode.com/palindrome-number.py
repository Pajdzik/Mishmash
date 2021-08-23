#!/bin/python3
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        stack = []

        while x > 0:
            d = x % 10
            stack.append(d)

            x = x // 10

        for i in range(len(stack) // 2):
            if stack[i] != stack[len(stack) - i - 1]:
                return False

        return True

Solution().isPalindrome(121)