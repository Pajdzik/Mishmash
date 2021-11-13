#!/bin/python3
# https://leetcode.com/problems/minimum-window-substring/

from typing import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = Counter(t)

        left = 0
        right = -1

        min_len = len(s)
        answer = ""

        matching = 0

        while right < len(s):
            if matching == len(t):
                if s[left] in chars:                    
                    chars[s[left]] += 1
                if chars[s[left]] > 0:
                    matching -= 1

                left += 1
            else:
                right += 1
                if right < len(s):
                    if chars[s[right]] > 0:
                        matching += 1
                    if s[right] in chars:
                        chars[s[right]] -= 1

            if matching == len(t):
                if right - left + 1 <= min_len:
                    min_len = right - left + 1
                    answer = s[left:right + 1]

        return answer

if __name__ == "__main__":
    assert(Solution().minWindow("a", "a") == "a")
    assert(Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC")