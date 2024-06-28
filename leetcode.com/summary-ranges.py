#!/bin/python3
# https://leetcode.com/problems/summary-ranges/


class Solution:

    def summaryRanges(self, nums: list[int]) -> list[str]:
        to_write = 0
        start = 0

        for i, el in enumerate(nums):
            if i + 1 >= len(nums) or el + 1 < nums[i + 1]:
                range = str(el) if start == i else f"{nums[start]}->{el}"
                nums[to_write] = range
                to_write += 1
                start = i + 1

        return nums[:to_write]

    def summaryRanges_additional_memory(self, nums: list[int]) -> list[str]:
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
