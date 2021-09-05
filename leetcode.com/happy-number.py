#!/bin/python3
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False
            else:
                visited.add(n)

            m = 0
            while n > 0:
                d = n % 10
                n = n // 10
                m += d**2

            n = m

        return True

Solution().isHappy(2)