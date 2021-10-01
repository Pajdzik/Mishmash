#!/bin/python3
# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: list[str]) -> int:
        start = 0
        delta = 0
        write = 0

        while start + delta < len(chars):
            while start + delta < len(chars) and chars[start + delta] == chars[start]:
                delta += 1
            
            chars[write] = chars[start]
            write += 1

            if delta > 1:
                count = str(delta)
                for i in range(len(count)):
                    chars[write] = count[i]
                    write += 1
            
            start = start + delta
            delta = 0

        return write

Solution().compress(["a","a","b","b","c","c","c"])
