#!/bin/python3
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()

        left = 0
        right = len(piles) - 2

        result = 0

        while left < right:
            result += piles[right]
            left += 1
            right -= 2

        return result


if __name__ == "__main__":
    assert Solution().maxCoins([2, 4, 1, 2, 7, 8]) == 9
    assert Solution().maxCoins([2, 4, 5]) == 4
    assert Solution().maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
