#!/bin/python3
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

from math import log


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        xor_result = nums[0]

        for n in nums[1:]:
            xor_result ^= n

        diff = xor_result ^ k
        if diff == 0:
            return 0

        result = 0
        for i in range(0, int(log(max(k, diff), 2)) + 2):
            if (1 << i) & diff > 0:
                result += 1

        return result


if __name__ == "__main__":

    def test(expected: int, input: list[int], k: int):
        result = Solution().minOperations(input, k)
        assert result == expected, f"{result} != {expected}"

    test(2, [2, 1, 3, 4], 1)
    test(1, [1, 3], 5)
