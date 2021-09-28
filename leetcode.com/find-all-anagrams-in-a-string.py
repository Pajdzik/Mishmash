#!/bin/python3
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_hist = Counter(p)
        s_hist = Counter()

        result = []
        for i in range(len(s)):
            new_c = s[i]
            s_hist[new_c] += 1

            if i - len(p) >= 0:
                old_c = s[i - len(p)]
                s_hist[old_c] -= 1

            match = True
            for letter, count in p_hist.items():
                if s_hist[letter] != count:
                    match = False

            if match:
                result.append(i - len(p) + 1)

        return result

Solution().findAnagrams("cbaebabacd", "abc")

