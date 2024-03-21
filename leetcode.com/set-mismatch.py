#!/bin/python3
# https://leetcode.com/problems/set-mismatch

from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        counter = Counter()

        for num in nums:
            counter[num] += 1

        dup = missed = None
        for i in range(1, len(nums) + 1):
            if counter[i] > 1:
                dup = i
            elif counter[i] == 0:
                missed = i

        return [dup, missed]


if __name__ == "__main__":
    def test(expected: list[int], nums: list[int]):
        result = Solution().findErrorNums(nums)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test([2, 1], [3, 2, 2])
    test([2, 3], [1, 2, 2, 4])
    test([1, 2], [1, 1])
    test([2, 1], [2, 2])
    test([3, 2], [3, 3, 1])
