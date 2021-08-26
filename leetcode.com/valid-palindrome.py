#!/bin/python3
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def is_alphanumeric(self, c: str):
        return (ord('0') <= ord(c) <= ord('9')) \
            or (ord('A') <= ord(c) <= ord('Z'))  \
            or (ord('a') <= ord(c) <= ord('z')) 

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > 0 and not s[r].isalnum():
                r -= 1

            if l > r:
                return True

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

Solution().isPalindrome("ab_a")