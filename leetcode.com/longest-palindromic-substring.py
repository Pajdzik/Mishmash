#!/bin/python3
# https://leetcode.com/problems/longest-palindromic-substring/

def get_palindrome(s, c, i, j):
    palindrome = [c]
    for d in range(1, min(i + 1, len(s) - j)):
        if s[i - d] == s[j + d]:
            palindrome.insert(0, s[i - d])
            palindrome.append(s[j + d])
        else:
            break

    return ''.join(palindrome)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''

        for i in range(len(s)):
            palindrome = [s[i]]

            palindrome = get_palindrome(s, s[i], i, i)
            if len(palindrome) > len(answer):
                answer = palindrome

            if i + 1 < len(s) and s[i + 1] == s[i]:
                palindrome = get_palindrome(s, s[i:i + 2], i, i + 1)
                if len(palindrome) > len(answer):
                    answer = palindrome

        return answer

Solution().longestPalindrome("tattarrattat")
