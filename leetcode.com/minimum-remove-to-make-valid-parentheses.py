#!/bin/python3
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cs = [c for c in s]
        count = 0

        for i, c in enumerate(cs):
            if c == "(":
                count += 1
            elif c == ")":
                if count == 0:
                    cs[i] = None
                else:
                    count -= 1

        count = 0
        for i in range(len(s) - 1, -1, -1):
            c = cs[i]
            if c == ")":
                count += 1
            elif c == "(":
                if count == 0:
                    cs[i] = None
                else:
                    count -= 1

        res = "".join(filter(lambda c: c is not None, cs))
        return res


if __name__ == "__main__":
    assert "ab(c)d"(Solution().minRemoveToMakeValid("a)b(c)d"))
    assert "lee(t(c)o)de"(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
