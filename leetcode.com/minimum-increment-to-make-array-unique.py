#!/bin/python3
# https://leetcode.com/problems/minimum-increment-to-make-array-unique

"""
[3,2,1,2,1,7]
[1,1,2,2,3,7]
[1,4,2,2,3,7] (3)
[1,4,2,5,3,7] (3) => 6
"""


class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        result = 0
        seen = set(nums)
        sorted_nums = sorted(nums)
        next_start = sorted_nums[0]

        for i, el in enumerate(sorted_nums):
            if i + 1 < len(sorted_nums) and sorted_nums[i + 1] == el:
                number = max(next_start, el + 1)
                while number in seen:
                    number += 1

                seen.add(number)
                result += number - el
                next_start = number + 1

        return result


if __name__ == "__main__":

    def test(expected: int, nums: list[int]):
        result = Solution().minIncrementForUnique(nums)
        assert result == expected, f"expected {expected}, but got {result}"

    test(1, [0, 2, 2])
    test(6, [3, 2, 1, 2, 1, 7])
    test(1, [1, 2, 2])
