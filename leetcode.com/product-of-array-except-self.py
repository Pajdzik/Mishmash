#!/bin/python3
# https://leetcode.com/problems/product-of-array-except-self

# Numbers: [1 2 3  4   5]
# Product of all: 120
# Product of all except self: [120 60 40 30 24]
# =>                [(1)*(120)       1*(60)      (1*2)*(20)     1*2*3*5      1*2*3*4]
# =>                [(1)*(2*3*4*5)   1*(3*4*5)   (1*2)*(4*5)   (1*2*3)*(5)   (1*2*3*4) * (1)]
# Numbers:          [1         2         3         4         5      ]
# Left products     [(1)       1         1*2       1*2*3     1*2*3*4   1*2*3*4*5]
# Right products    [1*2*3*4*5 2*3*4*5   3*4*5     4*5       5         (1)]
# Left products     [1 2 6    24 120]
# Right products    [120 60 20 5 1]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        found_zero = False

        left_products, product = [1], 1
        for num in nums:
            if num == 0:
                if found_zero:
                    return [0] * len(nums)
                found_zero = True

            product = product * num
            left_products.append(product)

        right_products, product = [1], 1
        for num in reversed(nums):
            product = product * num
            right_products.append(product)

        right_products.reverse()

        products = [
            l * r for (l, r) in zip(left_products[:-1], right_products[1:])]
        return products


if __name__ == "__main__":
    def test(expected: list[int], nums: list[int]):
        result = Solution().productExceptSelf(nums)
        assert result == expected, f"Expected: {expected}, but got: {result}"

    test([0, 2, 0], [1, 0, 2])
    test([120, 60, 40, 30, 24], [1, 2, 3, 4, 5])
    test([24, 12, 8, 6], [1, 2, 3, 4])
