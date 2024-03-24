#!/bin/python3
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] == arr[i + (len(arr) // 4)]:
                return arr[i]

        return -1


if __name__ == "__main__":
    def test(expected: int, arr: list[int]):
        result = Solution().findSpecialInteger(arr)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(6, [1, 2, 2, 6, 6, 6, 6, 7, 10])
