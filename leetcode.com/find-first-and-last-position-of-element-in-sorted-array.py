#!/bin/python3
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(delta: int) -> int:
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + ((right - left) // 2)

                if nums[middle] == target:
                    if not 0 <= middle + delta < len(nums) or nums[middle + delta] != target:
                        return middle
                    else:
                        if delta > 0:
                            left = middle + 1
                        else:
                            right = middle - 1

                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

            return -1

        start = binary_search(-1)
        end = binary_search(1)

        return [start, end]


if __name__ == "__main__":
    assert(Solution().searchRange([1], 1) == [0, 0])
    assert(Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])