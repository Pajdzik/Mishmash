#!/bin/python3
# https://leetcode.com/problems/sort-an-array

def merge(left_array: list[int], right_array: list[int]):
    result = []
    l = r = 0

    while l < len(left_array) or r < len(right_array):
        if l == len(left_array):
            result.append(right_array[r])
            r += 1
        elif r == len(right_array):
            result.append(left_array[l])
            l += 1
        else:
            if left_array[l] <= right_array[r]:
                result.append(left_array[l])
                l += 1
            else:
                result.append(right_array[r])
                r += 1

    return result

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return nums
    
    half_index = (len(nums) + 1) // 2
    left_array = nums[:half_index]
    right_array = nums[half_index:]

    sorted_left_array = merge_sort(left_array)
    sorter_right_array = merge_sort(right_array)

    return merge(sorted_left_array, sorter_right_array)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return merge_sort(nums)
    
if __name__ == "__main__":
    def test(expected: list[int], input: list[int]):
        # sort and compare the expected value
        result = Solution().sortArray(input)
        assert result == expected, f"Expected {expected} but got {result}"

    test([1, 2, 3, 4, 5], [5, 2, 3, 4, 1])