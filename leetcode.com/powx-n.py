#!/bin/python3
# https://leetcode.com/problems/powx-n/

class Solution:
    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x

        res = self.power(x, n // 2)
        if n % 2 == 0:
            return res * res
        else:
            return x * res * res
        
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0:
            return 1.0
        elif x == -1.0:
            return -1.0 if n > 0 else 1.0

        if n == 0:
            return 1.0
        elif n < 0:
            x = 1/x
            n = -n

        return self.power(x, n)
        

result = Solution().myPow(2.0, 10)
print(result)