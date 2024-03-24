#!/bin/python3
# https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        week = 1
        money = 0
        while n > 0:
            days_in_week = 7 if n >= 7 else n
            money += ((week + (week + days_in_week - 1)) * days_in_week) // 2
            week += 1
            n -= 7

        return money


if __name__ == "__main__":
    def test(expected: int, n: int):
        result = Solution().totalMoney(n)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(10, 4)
    test(37, 10)
    test(96, 20)
