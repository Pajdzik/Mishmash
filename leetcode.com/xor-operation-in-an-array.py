#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional

"""
start + 2i

x + 00000
x + 00010
x + 00100
x + 00110
x + 01000
x + 01010
x + 01100
x + 01110
x + 10000

"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = start

        for i in range(1, n):
            s = s ^ (start + 2 * i)

        return s


if __name__ == "__main__":
    pass
