#!/bin/python3
# https://leetcode.com/problems/jewels-and-stones/

from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        return sum(c[jewel] for jewel in jewels)
