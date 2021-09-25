#!/bin/python3
# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
            
        queue = []
        cache = set()

        for num in nums:
            if num in cache:
                return True
            
            queue.append(num)
            
            if len(queue) > k:
                el = queue.pop(0)
                cache.remove(el)
            
            cache.add(num)

        return False


    def containsNearbyDuplicate_bf(self, nums: list[int], k: int) -> bool:
        for i in range(0, len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True

        return False

Solution().containsNearbyDuplicate([1,2,3,1], 3)