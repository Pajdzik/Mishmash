#!/bin/python3
# https://leetcode.com/problems/subarray-sum-equals-k/

from unittest import result


class Solution:
    def subarraySum(self, numbers: list[int], k: int) -> int:
        result = 0

        partial_sum = 0
        partial_sums = { }

        for i, number in enumerate(numbers):
            partial_sum += number

            if partial_sum == k:
                result += 1
            if partial_sum - k in partial_sums:
                result += partial_sums[partial_sum - k]
            if number == k:
                result += 1

            if partial_sum in partial_sums:
                partial_sums[partial_sum] += 1
            else:
                partial_sums[partial_sum] = 1

        return result

if __name__ == "__main__":
    assert(Solution().subarraySum([1, 2, 3], 3) == 2)
    assert(Solution().subarraySum([1,-1,0], 0) == 1)
    assert(Solution().subarraySum([-1,-1,1], 0) == 1)