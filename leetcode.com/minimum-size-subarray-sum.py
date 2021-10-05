#!/bin/python3
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        min_length = len(nums) + 1
        sum = nums[0]

        while left < len(nums):
            if sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
            elif sum < target and right < len(nums) - 1:
                right += 1
                sum += nums[right]
            else:
                break

        return min_length if min_length != len(nums) + 1 else 0

if __name__ == "__main__":
    Solution().minSubArrayLen(15, [1,2,3,4,5])
    