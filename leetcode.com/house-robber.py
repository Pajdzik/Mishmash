#!/bin/python3
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int], index: int = 0, earnings: int = 0, cache: dict[int, int] = {}) -> int:
        if index >= len(nums):
            return earnings
        
        if index in cache:
            return cache[index]

        taking = self.rob(nums, index + 2, earnings + nums[index], cache)
        avoiding = self.rob(nums, index + 1, earnings, cache)
        cache[index] = max(taking, avoiding)

        return cache[index]

    def rob_from_the_end(self, nums: list[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if i + 2 < len(nums):
                nums[i] = max(nums[i + 1], nums[i + 2] + nums[i])
            else:
                nums[i] = max(nums[i], nums[i + 1])

        return nums[0]

    def find_backtracking(self, nums: list[int], index: int, value: int) -> int:
        max_value = value
        for i in range(index + 2, len(nums)):
            new_value = value + self.find(nums, i, value)
            max_value = max(max_value, new_value)

        return max_value + nums[index]

if __name__ == "__main__":
    result = Solution().rob([2,7,9,3,1])
    print(result)