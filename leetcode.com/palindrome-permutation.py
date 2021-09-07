#!/bin/python3
# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        odd_filled = False
        for key in counter:
            if counter[key] % 2 == 1:
                if odd_filled:
                    return False
                else:
                    odd_filled = True

        return True

Solution().canPermutePalindrome("code")