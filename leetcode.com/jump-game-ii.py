#!/bin/python3
# https://leetcode.com/problems/jump-game-ii/

import re


class Solution:
    def jump(self, numbers: list[int]) -> int:
        if len(numbers) <= 1:
            return 0

        jumps = 0
        reach = 0
        max_jump = 0

        for i in range(len(numbers) - 1):
            reach = max(reach, i + numbers[i])
            if i == max_jump:
                jumps += 1
                max_jump = reach
                reach = 0
        
        return jumps

if __name__ == "__main__":
    result = Solution().jump([2,3,1,1,4])
    print(result)

