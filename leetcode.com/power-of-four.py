#!/bin/python3
# hhttps://leetcode.com/problems/power-of-four


from typing import List, Optional


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            nn = n / 4
            if int(nn) < nn:
                print(nn)
                return False
            n = int(nn)

        return True


if __name__ == "__main__":
    pass
