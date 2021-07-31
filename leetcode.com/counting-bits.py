#!/bin/python3
# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0, 1, 1, 2]
        vector_length = 2
        start = len(bits)
        
        while start <= n:
            bits.extend(bits[start - vector_length:start])
            bits.extend([x + 1 for x in bits[start - vector_length:start]])
            vector_length *= 2
            start += vector_length
                
        return bits[:n + 1]

print(Solution().countBits(4))