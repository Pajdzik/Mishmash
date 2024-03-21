#!/bin/python3
# https://leetcode.com/problems/count-elements-with-maximum-frequency

from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counter = Counter(nums)
        _, max_count = counter.most_common(1)[0]
        max_counts = filter(lambda c: c == max_count, counter.values())
        return sum(max_counts)


if __name__ == "__main__":
    def test(expected: int, nums: list[int]):
        result = Solution().maxFrequencyElements(nums)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(4, [1, 2, 2, 3, 1, 4])
    test(5, [1, 2, 3, 4, 5])
