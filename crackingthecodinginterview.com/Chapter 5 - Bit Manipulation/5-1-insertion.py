#!/usr/bin/env python3

# You are given two 32-bit numbers, N and M, and two bit positions, i and j.
# Write a method to insert M into N such that M starts at bit j and ends at bit i.
# You can assume that the bits j through i have enough space to fit all of M.
# That is, if M = 10011, you can assume that there are at least 5 bits between j and i.
# You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
# 10000000000
#     10011    (2 - 6)
# 10001001100

from _bit import print_binary, binary_array_to_number

def insert(m, n, i, j):
    mask = 0xFFFF
    mask = (mask >> (16 - j)) << i
    mask = mask ^ 0xFFFF

    m = m & mask
    n = n << i

    return m ^ n # or m + n

if __name__ == "__main__":
    m = binary_array_to_number("10000000000")
    n = binary_array_to_number("10011")
    o = binary_array_to_number("10001001100")

    oo = insert(m, n, 2, 6)
    print(oo)
    pass