#!/usr/bin/env python3

# Given a positive integer, print the next smallest and the next largest
# number that have the same number of 1 bits in their binary representation.

from _bit import print_binary

def find_bit(n, value, from_bit=0):
    for bit in range(from_bit, 33):
        if n & (value << bit) == (value << bit):
            return bit

    return None

def next_number(n):
    rightmost_one = find_bit(n, 1)
    rightmost_zero = find_bit(n, 0, rightmost_one)

    n = n ^ (1 << rightmost_one)
    n = n ^ (1 << rightmost_zero)
    
    return n

if __name__ == "__main__":
    n = 0x7AB4
    print_binary(n)
    next_n = next_number(n)
    print_binary(next_n)