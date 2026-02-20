#!/bin/python3
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array


from typing import List, Optional


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        found = [False] * len(nums)

        for num in nums:
            found[num - 1] = True

        return [n + 1 for n in range(len(nums)) if not found[n]]


if __name__ == "__main__":
    pass
