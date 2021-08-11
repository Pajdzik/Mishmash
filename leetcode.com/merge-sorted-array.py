#!/bin/python3
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        insert_index = m + n - 1
        index1 = m - 1
        index2 = n - 1

        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        while insert_index >= 0:
            if index1 >= 0 and nums1[index1] >= nums2[index2]:
                nums1[insert_index] = nums1[index1]
                index1 -= 1
            elif index2 >= 0:
                nums1[insert_index] = nums2[index2]
                index2 -= 1
            else:
                break
            
            insert_index -= 1

nums = [0]
Solution().merge(nums, 0, [1], 1)
pass