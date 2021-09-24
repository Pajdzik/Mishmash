#!/bin/python3
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
            
        for i in range(len(cost) - 1):
            cost2 = cost[i - 2] if i - 2 >= 0 else 0
            cost1 = cost[i - 1] if i - 1 >= 0 else 0
            cost[i] = min(cost2, cost1) + cost[i]

        return min(cost[-3] + cost[-1], cost[-2])

Solution().minCostClimbingStairs([])