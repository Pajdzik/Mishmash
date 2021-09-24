#!/bin/python3
# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        cache = { }

        for num in nums:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

        previous_number = None
        taking = 0
        avoiding = 0

        for num, count in sorted(cache.items()):
            earning = num * count

            if previous_number == num - 1:
                avoiding, taking = taking, max(taking, avoiding + earning)
            else:
                avoiding, taking = taking, max(avoiding, taking) + earning
            
            previous_number = num

        return max(avoiding, taking)

Solution().deleteAndEarn([3,4,2])