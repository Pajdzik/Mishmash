#!/bin/python3
# https://leetcode.com/problems/smallest-even-multiple/


from typing import List, Optional


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2


if __name__ == "__main__":
    pass
