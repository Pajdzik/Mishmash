#!/bin/python3
# https://leetcode.com/problems/valid-palindrome-ii/

from typing import Tuple

class Solution:
    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        i = start
        j = end
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.isPalindrome(s, i + 1, j) or self.isPalindrome(s, i, j - 1)
        
        return True

result = Solution().validPalindrome("abc")
print(result)