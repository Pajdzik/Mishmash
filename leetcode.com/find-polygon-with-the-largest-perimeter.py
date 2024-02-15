#!/bin/python3
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

# [1 12 1 2 5 50 3]

# [1 1 2 3 5  12 50]
# [1 2 4 7 12 24 74]

# [5 5  5]
# [5 10 15]

# [1, 1, 2, 3, 5,  12, 50, 1000000001]
# [1, 2, 4, 7, 12, 24, 74]

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        sum_of_nums = sum(nums)

        for i in range(len(sorted_nums) - 1, 1, -1):
            sum_of_nums -= sorted_nums[i]

            if sum_of_nums > sorted_nums[i]:
                return sum_of_nums + sorted_nums[i]

        return - 1


if __name__ == "__main__":
    def check(expected: int, nums: list[int]):
        result = Solution().largestPerimeter(nums)
        if result != expected:
            print(f'Expected: {expected}; Result: {result}')
            assert False

    check(12, [1, 12, 1, 2, 5, 50, 3])
    check(15, [5, 5, 5])
