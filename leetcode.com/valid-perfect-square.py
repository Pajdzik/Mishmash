#!/bin/python3
# https://leetcode.com/problems/valid-perfect-square

from typing import List, Optional


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        start = 1
        end = num // 2

        while start <= end:
            n = start + ((end - start) // 2)
            nn = n * n
            if nn == num:
                return True

            if nn > num:
                end = n - 1
            else:
                start = n + 1

        return False

    def isPerfectSquare2(self, num: int) -> bool:
        n = 1
        nn = 1

        while nn <= num:
            if nn == num:
                return True

            n += 1
            nn = n * n

        return False


if __name__ == "__main__":
    assert Solution().isPerfectSquare(1)
    assert not Solution().isPerfectSquare(14)
