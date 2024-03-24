#!/bin/python3
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1, max2 = 0, 0
        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num >= max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    def test(expected: int, nums: list[int]):
        result = Solution().maxProduct(nums)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(36, [10, 2, 5, 2])
    test(12, [3, 4, 5, 2])
    test(16, [1, 5, 4, 5])
