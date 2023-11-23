#!/bin/python3
# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for i in range(0, n):
            result.append(nums[i])
            result.append(nums[i + n])

        return result


if __name__ == "__main__":
    def test(expected: list[int], nums: list[int], n: int):
        result = Solution().shuffle(nums, n)
        if expected != result:
            raise AssertionError(f'Expected {expected} was {result}')

    test([2, 3, 5, 4, 1, 7], [2, 5, 1, 3, 4, 7], 3)
"""
[2, 5, 1, 3, 4, 7]
[0, 1, 2, 3, 4, 5]
[0, 3, 1, 4, 2, 5] 

[0, 1, 2, 3, 4, 5, 6, 7]
[0, 4, 1, 5, 2, 6, 3, 7]
"""
