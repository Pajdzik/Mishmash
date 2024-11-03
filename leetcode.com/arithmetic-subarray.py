#!/bin/python3
# https://leetcode.com/problems/arithmetic-subarrays

from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        result = []
        for i in range(len(l)):
            subarray = sorted(nums[l[i] : r[i] + 1])
            diff = subarray[1] - subarray[0]

            res = True
            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j - 1] != diff:
                    res = False
                    break

            result.append(res)
        return result


def main():
    def assert_equals(expected, actual):
        assert expected == actual, f"Expected {expected}, but got {actual}"

    solution = Solution()
    # Test case 1
    assert_equals(
        [True, False, True],
        solution.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]),
    )

    # Test case 2
    assert_equals(
        [True, True], solution.checkArithmeticSubarrays([1, 2, 3, 4], [0, 1], [2, 3])
    )

    print("All test cases passed.")


if __name__ == "__main__":
    main()
