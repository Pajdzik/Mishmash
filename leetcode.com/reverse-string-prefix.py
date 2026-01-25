#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return "".join((reversed(s[:k]))) + s[k:]


if __name__ == "__main__":
    pass
