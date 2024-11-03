#!/bin/python3
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets

from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def calc_or(l: List[int]) -> int:
            or_res = 0
            for num in l:
                or_res = or_res | num
            return or_res

        max_or = calc_or(nums)

        result = 0

        def check_subsets(subset: List[int], start_index: int):
            nonlocal result
            subset_or = calc_or(subset)
            if subset_or == max_or:
                result += 1

            for i in range(start_index, len(nums)):
                subset.append(nums[i])
                check_subsets(subset, i + 1)
                subset.pop()

        check_subsets([], 0)
        return result


def main():
    sol = Solution()
    assert sol.countMaxOrSubsets([3, 2, 1, 5]) == 6
    assert sol.countMaxOrSubsets([3, 1]) == 2
    assert sol.countMaxOrSubsets([2, 2, 2]) == 7


if __name__ == "__main__":
    main()
