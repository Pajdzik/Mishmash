#!/bin/python3
# https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        result_digits = []
        removed_elements = 0

        for d in num:
            while result_digits \
                    and removed_elements < k \
                    and d < result_digits[-1]:
                result_digits.pop()
                removed_elements += 1

            if result_digits or d != '0':
                result_digits.append(d)

        while result_digits and removed_elements < k:
            result_digits.pop()
            removed_elements += 1

        result_number = ''.join(result_digits).lstrip('0')
        return result_number if result_number else "0"


if __name__ == "__main__":
    def test(num, k, expected):
        result = Solution().removeKdigits(num, k)
        assert (result == expected), f"{result} != {expected}"

    test("10001", 4, "0")
    test("112", 1, "11")
    test("1432219", 3, "1219")
    test("10200", 1, "200")
    test("10", 2, "0")
    test("9", 1, "0")

'''

1432219 3
 xxx
1   219

t = len(n) - k = 4

1: [ 1 ]      -- empty (remaining digits 6)
4: [ 1 4 ]    -- 1 < 4 (remaining digits 5)
3: [ 1 3 ]    -- 4 > 3 (remaining digits 4)
2: [ 1 2 ]    -- 3 > 2 (remaining digits 3)
2: [ 1 2 2 ]  -- 2 = 2 (remaining digits 2)
1: [ 1 2 1 ]  -- 2 > 1 (remaining digits 1) (t can still be met)
9: [ 1 2 1 9] -- 1 < 9

----
10200 1
x
 0200

10 2
xx
  0

  

'''
