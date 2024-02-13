#!/bin/python3
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def is_palindrome(word: str) -> bool:
            start = 0
            end = len(word) - 1

            while start <= end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1

            return True

        for word in words:
            if is_palindrome(word):
                return word

        return ""


if __name__ == "__main__":
    assert Solution().firstPalindrome(["ada", "abc", "bbb"]) == "ada"
