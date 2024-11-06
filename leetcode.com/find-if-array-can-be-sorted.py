#!/bin/python3
# https://leetcode.com/problems/find-if-array-can-be-sorted

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(num: int) -> int:
            result = 0
            mask = 1
            while mask <= num:
                if num & mask:
                    result += 1
                mask <<= 1

            return result

        bits = [count_bits(num) for num in nums]

        previous_segment_max = 0
        segment_max = nums[0]

        for i in range(1, len(nums)):
            if bits[i] != bits[i - 1]:
                previous_segment_max = segment_max
                segment_max = nums[i]
            else:
                segment_max = max(segment_max, nums[i])

            if nums[i] < previous_segment_max:
                return False

        return True


def test(expected: bool, nums: List[int]):
    solution = Solution()
    result = solution.canSortArray(nums)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    test(False, [3, 16, 8, 4, 2])
    test(True, [8, 4, 2, 30, 15])
