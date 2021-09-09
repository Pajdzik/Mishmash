#!/bin/python3
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version) -> bool:
    return version >= 4

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        
        while True:
            middle = l + ((r - l) // 2)
            if isBadVersion(middle):
                if not isBadVersion(middle - 1):
                    return middle
                r = middle - 1
            else:
                l = middle + 1

    
Solution().firstBadVersion(5)