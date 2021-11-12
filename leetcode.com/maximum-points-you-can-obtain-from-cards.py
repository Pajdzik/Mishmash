#!/bin/python3
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        sum = 0
        
        for i in range(k):
            sum += cardPoints[i]

        max_sum = sum

        for i in range(k):
            sum = sum - cardPoints[k - 1 - i] + cardPoints[len(cardPoints) - 1 - i]
            max_sum = max(max_sum, sum)

        return max_sum

if __name__ == "__main__":
    assert(Solution().maxScore([1,2,3,4,5,6,1], 3) == 12)