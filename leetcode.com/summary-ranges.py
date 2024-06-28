#!/bin/python3
# https://leetcode.com/problems/summary-ranges/


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        i = 0

        while i < len(nums):
            min = nums[i]
            max = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
                max = nums[i]
            else:
                i += 1

            range = str(min) if min == max else f"{min}->{max}"
            ranges.append(range)

        return ranges


if __name__ == "__main__":

    def test(expected: list[str], nums: list[int]):
        result = Solution().summaryRanges(nums)
        assert result == expected, f"expected {expected}, but got {result}"

    test(["0->2"], [0, 1, 2])
    test(["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9])
