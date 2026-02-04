#!/bin/python3
# https://leetcode.com/problems/reverse-degree-of-a-string/description/


from typing import List, Optional


class Solution:
    def reverseDegree(self, s: str) -> int:
        vals = [ord("z") - ord(c) + 1 for c in s]
        return sum([el * (i + 1) for el, i in zip(vals, range(len(s)))])


if __name__ == "__main__":
    assert Solution().reverseDegree("abc") == 148
