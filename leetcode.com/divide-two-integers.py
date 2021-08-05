class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1 if (dividend >= 0 and divisor >= 0) \
            or (dividend < 0 and divisor < 0) else -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        while dividend >= divisor:
            dividend -= divisor
            result += 1

        return sign * result

Solution().divide(10, 3)