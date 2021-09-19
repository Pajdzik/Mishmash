#!/bin/python3
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sum_of_lens = len(nums1) + len(nums2)
        median_index = sum_of_lens // 2
        median_index1, median_index2 = median_index, median_index
        if sum_of_lens % 2 == 0:
            median_index1 -= 1

        m1, m2 = None, None
        i1 = 0
        i2 = 0

        while m2 == None:
            if i2 >= len(nums2) or (i1 < len(nums1) and nums1[i1] < nums2[i2]):
                if i1 + i2 == median_index1:
                    m1 = nums1[i1]

                if i1 + i2 == median_index2:
                    m2 = nums1[i1] 

                i1 += 1
            elif i1 >= len(nums1) or i2 < len(nums2):
                if i1 + i2 == median_index1:
                    m1 = nums2[i2]

                if i1 + i2 == median_index2:
                    m2 = nums2[i2] 

                i2 += 1

        return (m1 + m2) / 2


result = Solution().findMedianSortedArrays([1,3], [2])
print(result)