#!/bin/python3
# https://leetcode.com/problems/hand-of-straights/

from typing import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        counted_hand = Counter(hand)
        
        for c in sorted(hand):
            if counted_hand[c] == 0:
                continue

            for next in range(c, c + groupSize):
                if next not in counted_hand or counted_hand[next] == 0:
                    return False
                else:
                    counted_hand[next] -= 1

        return True

if __name__ == "__main__":
    Solution().isNStraightHand([1,1,2,2,3,3], 3)