#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [i + extraCandies >= max_candies for i in candies]


if __name__ == "__main__":
    pass
