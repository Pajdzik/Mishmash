#!/bin/python3
# https://leetcode.com/problems/permutations/

def generate_permutation(index: int, nums: list[int], permutations: list[list[int]]):
    if index == 1:
        permutations.append(nums.copy())
    else:
        generate_permutation(index - 1, nums, permutations)
        for i in range(0, index - 1):
            if index % 2 == 0:
                nums[i], nums[index - 1] = nums[index - 1], nums[i]
            else:
                nums[0], nums[index - 1] = nums[index - 1], nums[0]

            generate_permutation(index - 1, nums, permutations)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []
        generate_permutation(len(nums), nums, permutations)

        return permutations

Solution().permute([1, 2, 3])