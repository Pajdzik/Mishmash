#!/bin/python3
# https://leetcode.com/problems/goal-parser-interpretation/


from typing import List, Optional


class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0

        while i < len(command):
            if command[i] == "(":
                i += 1
                if command[i] == ")":
                    res.append("o")
                else:
                    i += 2
                    res.append("al")
            elif command[i] == "G":
                res.append("G")

            i += 1

        return "".join(res)


if __name__ == "__main__":
    assert Solution().interpret("(al)G(al)()()G") == "alGalooG"
