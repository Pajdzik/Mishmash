#!/bin/python3
# https://leetcode.com/problems/longest-increasing-subsequence

from typing import List

# [10, 9, 2, 5, 3, 7, 101, 18]
# [1,  1, 1, 2, 2, 3,   4,  4]

# starting lengths of subsequences
# [1,  1, 1, 1, 1, 1,   1,   1]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


if __name__ == "__main__":

    def test(expected: int, nums: List[int]):
        sol = Solution()
        result = sol.lengthOfLIS(nums)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Test cases
    test(4, [10, 9, 2, 5, 3, 7, 101, 18])
    test(4, [0, 1, 0, 3, 2, 3])
    test(1, [7, 7, 7, 7, 7, 7, 7])
    test(3, [4, 10, 4, 3, 8, 9])
