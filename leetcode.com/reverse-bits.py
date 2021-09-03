#!/bin/python3
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        ii = bin(n)
        for i in range(0, 16):
            l_mask = (1 << (32 - i - 1))
            r_mask = (1 << i)
            l = n & l_mask
            r = n & r_mask

            if l > 0:
                n = n | r_mask
            else:
                n = n & ~r_mask

            if r > 0:
                n = n | l_mask
            else:
                n = n & ~l_mask

        nn = bin(n)
        return n

#       1928352384 (01110010111100000101001010000000)
#       1928352384 (01110010111100000101001010000000)
#        964176192 (00111001011110000010100101000000)

Solution().reverseBits(43261596)