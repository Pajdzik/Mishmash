#!/bin/python3
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest_queue(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            if (len(heap) < k) or heap[k - 1] < num:
                i = 0
                while i < len(heap):
                    if num >= heap[i]:
                        break
                    i += 1

                heap.insert(i, num)

        return heap[k - 1]

    def findKthLargest_simple(self, nums: list[int], k: int) -> int:
        skip = []
        for t in range(k):
            max = -10*5
            max_i = None

            for i, el in enumerate(nums):
                if i not in skip and el > max:
                    max_i, max = i, el

            if t == k - 1:
                return max
            else:
                skip.append(max_i)

Solution().findKthLargest([2, 1], 2)