#!/bin/python3
# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def str_representation(base: int) -> str:
            representation = []
            number = n

            while number > 0:
                representation.append(number % base)
                number //= base

            # no need to flip
            return str(representation)

        def is_palindrome(n: str) -> bool:
            for i in range(0, len(n) // 2):
                if n[0] != n[len(n) - i - 1]:
                    return False

            return True

        return all([is_palindrome(str_representation(base)) for base in range(2, n - 2 + 1)])


if __name__ == "__main__":
    assert Solution().isStrictlyPalindromic(4) == False
    assert Solution().isStrictlyPalindromic(1) == True
