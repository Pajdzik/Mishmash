#!/bin/python3
# https://leetcode.com/problems/maximum-subarray    

import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def max_sum(left: int, right: int):
            if right < left:
                return -math.inf
            if right == left:
                return nums[left]
            
            mid = (left + right) // 2
            left_sum, curr_sum = 0, 0
            for i in range(mid - 1, left - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)

            right_sum, curr_sum = 0, 0
            for i in range(mid + 1, right + 1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)

            best_left = max_sum(left, mid - 1)
            best_right = max_sum(mid + 1, right)

            return max(best_left, best_right, left_sum + nums[mid] + right_sum)
        
        return max_sum(0, len(nums) - 1)



    def maxSubArray_dp(self, nums: list[int]) -> int:
        max_subarray = nums[0]
        curr_subarray = 0

        for i, num in enumerate(nums):
            curr_subarray = max(num, curr_subarray + num if i > 0 else num)
            max_subarray = max(max_subarray, curr_subarray)

        return max_subarray
    
if __name__ == "__main__":
    assert(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)