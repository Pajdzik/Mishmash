#!/bin/python3
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0, 1, 2]

        for step in range(3, n + 1):
            steps.append(steps[step - 1] + steps[step - 2])

        return steps[n]

Solution().climbStairs(38)