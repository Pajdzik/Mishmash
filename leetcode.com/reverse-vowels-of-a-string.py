#!/bin/python3
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        res = [ c for c in s ]

        vowels = { 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U' }

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1

            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return ''.join(res)

if __name__ == "__main__":
    assert(Solution().reverseVowels("aA") == "Aa")