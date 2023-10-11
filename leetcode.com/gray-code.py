#!/bin/python3
# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> list[int]:
        codes = [0, 1]
        i = 1

        while i < n:
            one_prefix = [x | (1 << i) for x in reversed(codes)]
            codes = codes + one_prefix
            i + 1

        return codes


if __name__ == "__main__":
    def test_and_print_failure(n: int, expected: list[int]):
        res = Solution().grayCode(n)

        if res != expected:
            print(f'Incorrect result for {n}: {res}')

    test_and_print_failure(2, [0, 1, 3, 2])

'''
2 => [0, 1, 3, 2] => [00, 01, 11, 10]
3 => [000, 001, 011, 010, 110, 111, 101, 100]

'''
