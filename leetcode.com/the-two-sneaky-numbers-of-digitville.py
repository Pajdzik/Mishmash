#!/bin/python3
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

from typing import Counter, List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        result = c.most_common(2)
        return [result[0][0], result[1][0]]


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 2, 3, 3, 3]
    print(solution.getSneakyNumbers(nums1))  # Output: [3, 2]

    # Test case 2
    nums2 = [4, 4, 4, 5, 5, 6]
    print(solution.getSneakyNumbers(nums2))  # Output: [4, 5]

    # Test case 3
    nums3 = [7, 8, 8, 9, 9, 9, 10, 10, 10, 10]
    print(solution.getSneakyNumbers(nums3))  # Output: [10, 9]

    # Test case 4
    nums4 = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    print(solution.getSneakyNumbers(nums4))  # Output: [3, 1]
