#!/bin/python3
# https://leetcode.com/problems/


from typing import List, Optional


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        found = set()
        taken = [False] * len(tiles)

        letters = []

        def next(index: int):
            if index >= len(tiles):
                return
            for i in range(len(tiles)):
                if taken[i]:
                    continue

                taken[i] = True
                letters.append(tiles[i])

                found.add("".join(letters))
                next(index + 1)

                letters.pop()
                taken[i] = False

        next(0)
        return len(found)


if __name__ == "__main__":
    assert Solution().numTilePossibilities("AAB") == 8
    pass
