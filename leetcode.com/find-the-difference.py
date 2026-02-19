#!/bin/python3
# https://leetcode.com/problems/find-the-difference

from typing import Counter, List, Optional


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for c in t_counter.keys():
            if s_counter[c] != t_counter[c]:
                return c

        raise "This shouldn't happen"


if __name__ == "__main__":
    pass
