#!/bin/python3
# https://leetcode.com/problems/majority-element/
# https://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_num = None
        count = 0

        for num in nums:
            if count == 0:
                majority_num = num
                count += 1
            else:
                if majority_num == num:
                    count += 1
                else:
                    count -= 1
        
        return majority_num