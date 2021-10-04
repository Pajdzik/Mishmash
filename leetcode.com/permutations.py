#!/bin/python3
# https://leetcode.com/problems/permutations/

def generate_permutation_heap(index: int, nums: list[int], permutations: list[list[int]]):
    if index == 1:
        permutations.append(nums.copy())
    else:
        generate_permutation_heap(index - 1, nums, permutations)
        for i in range(0, index - 1):
            if index % 2 == 0:
                nums[i], nums[index - 1] = nums[index - 1], nums[i]
            else:
                nums[0], nums[index - 1] = nums[index - 1], nums[0]

            generate_permutation_heap(index - 1, nums, permutations)

class Solution:
    def permute_recursively(self, nums: list[int], permutation: list[int], taken: list[bool], results: list[list[int]]) -> None:
        if len(permutation) == len(nums):
            results.append(permutation[:])
        else:
            for i, num in enumerate(nums):
                if taken[i] == True:
                    continue

                taken[i] = True
                permutation.append(num)
                self.permute_recursively(nums, permutation, taken, results)
                permutation.remove(num)
                taken[i] = False

    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []
        self.permute_recursively(nums, [], [False] * len(nums), permutations)
        return permutations

Solution().permute([1, 2, 3])