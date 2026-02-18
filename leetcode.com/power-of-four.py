#!/bin/python3
# hhttps://leetcode.com/problems/power-of-four


from typing import List, Optional

# 4, 16, 64, 256, 1024, 4096
# 0b100
# 0b10000
# 0b1000000
# 0b100000000

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bin_n_with_prefix = bin(n)
        bin_n = bin_n_with_prefix[2:]
        one, zeroes = bin_n[0], bin_n[1:]

        return one == "1" and len(zeroes) & 1 == 0 and all([c == "0" for c in zeroes])

    def isPowerOfFour2(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            nn = n / 4
            if int(nn) < nn:
                print(nn)
                return False
            n = int(nn)

        return True


if __name__ == "__main__":
    Solution().isPowerOfFour(64)
