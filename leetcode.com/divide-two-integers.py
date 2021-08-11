#!/bin/python3
# https://leetcode.com/problems/divide-two-integers/

def count_bits(n: int) -> int:
    bit_count = 0
    while n > 0:
        n >>= 1
        bit_count += 1

    return bit_count

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend == -2**31:
                return (2**31 - 1)
            return -dividend
        
        result = 0
        negative = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            count = 1
            temp_divisor = divisor

            while dividend >= temp_divisor:
                count <<= 1
                temp_divisor <<= 1

            result += (count >> 1)
            dividend -= (temp_divisor >> 1)

        return -result if negative else result 

    def divide_simple(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1 if (dividend >= 0 and divisor >= 0) \
            or (dividend < 0 and divisor < 0) else -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= divisor:
            dividend -= divisor
            result += 1

        return sign * result

    

res = Solution().divide(-2147483648, -1)
exp = 1124222 // 34
pass