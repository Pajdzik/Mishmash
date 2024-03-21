#!/bin/python3
# https://leetcode.com/problems/minimum-common-value

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i1, i2 = 0, 0

        while True:
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] > nums2[i2]:
                i2 += 1
                if i2 >= len(nums2):
                    return -1
            else:
                i1 += 1
                if i1 >= len(nums1):
                    return -1


if __name__ == "__main__":
    def test(expected: int, nums1: list[int], nums2: list[int]):
        result = Solution().getCommon(nums1, nums2)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test(2, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    test(1, [1, 2, 3, 4, 5], [1, 3, 4, 5, 6])
