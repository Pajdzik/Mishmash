#!/bin/python3
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

from typing import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k > 0:
            return False

        counted_hand = Counter(nums)
        
        for c in sorted(nums):
            if counted_hand[c] == 0:
                continue

            for next in range(c, c + k):
                if next not in counted_hand or counted_hand[next] == 0:
                    return False
                else:
                    counted_hand[next] -= 1

        return True

if __name__ == "__main__":
    Solution().isNStraightHand([1,1,2,2,3,3], 3)