#!/bin/python3
# https://leetcode.com/problems/transform-array-by-parity/description/


from typing import List, Optional


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd_count, even_count = 0, 0

        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return ([0] * even_count) + ([1] * odd_count)


if __name__ == "__main__":
    pass
