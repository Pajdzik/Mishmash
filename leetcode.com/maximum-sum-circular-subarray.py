#!/bin/python3
# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max_sum = nums[0]
        max_sum = nums[0]

        curr_min_sum = nums[0]
        min_sum = nums[0]

        total_sum = nums[0]

        for i in range(1, len(nums)):
            el = nums[i]
            total_sum += el

            curr_max_sum = max(curr_max_sum + el, el)
            curr_min_sum = min(curr_min_sum + el, el)

            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum


if __name__ == "__main__":

    def test(expected: int, nums: List[int]):
        sol = Solution()
        result = sol.maxSubarraySumCircular(nums)
        assert result == expected, f"Expected {expected}, but got {result}"

    # Test cases
    test(10, [5, -3, 5])
    test(3, [1, -2, 3, -2])
    test(4, [3, -1, 2, -1])
    test(3, [3, -2, 2, -3])
    test(-1, [-2, -3, -1])
