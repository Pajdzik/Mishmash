#!/bin/python3
# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        start = 0
        product = 1
        count = 0

        for end, c in enumerate(nums):
            product *= c

            while start <= end and product >= k:
                product //= nums[start]
                start += 1

            count += end - start + 1

        return count

Solution().numSubarrayProductLessThanK([10,5,2,6], 100)