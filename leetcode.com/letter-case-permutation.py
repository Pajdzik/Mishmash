#!/bin/python3
# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation_recursive(self, results: list[list[str]], s: str, i: int):
        new_results = []

        while len(results) > 0:
            result = results.pop()

            if s[i].isalpha():
                new_results.append(result + [s[i].lower()])
                new_results.append(result + [s[i].upper()])
            else:
                new_results.append(result + [s[i]])

        if i + 1 < len(s):
            return self.letterCasePermutation_recursive(new_results, s, i + 1)
        else:
            return [ ''.join(result) for result in new_results ]

    def letterCasePermutation(self, s: str) -> list[str]:
        return self.letterCasePermutation_recursive([[]], s, 0)

    def letterCasePermutation_bitmask(self, s: str) -> list[str]:
        result = []
        word = []
        mask_length = 0
        for c in s:
            word.append(c)
            if c.isalpha():
                mask_length += 1
        
        for mask in range(0, 2**mask_length):
            c = 0
            for i in range(len(word)):
                if word[i].isalpha():
                    if mask & (1 << c):
                        word[i] = word[i].upper()
                    else:
                        word[i] = word[i].lower()

                    c += 1

            result.append(''.join(word))

        return result

Solution().letterCasePermutation("a23vs2")