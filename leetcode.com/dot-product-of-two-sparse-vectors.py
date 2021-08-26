#!/bin/python3
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector:
    def __init__(self, nums: list[int]):
        self.values = {}

        for i, num in enumerate(nums):
            if num != 0:
                self.values[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for index in self.values.keys():
            if index in vec.values:
                result += self.values[index] * vec.values[index]

        return result

vec1 = SparseVector([0,0,0,0,0,0,3,0,0,3,0,0,0])
vec2 = SparseVector([0,0,2,0,0,4,3,0,0,2,0,0,0])
dot = vec1.dotProduct(vec2)
print(dot)