#!/bin/python3
# https://leetcode.com/problems/valid-parenthesis-string

import functools


class Solution:
    def checkValidString(self, s: str) -> bool:
        @functools.lru_cache(None)
        def match(s: str, opened_parenthesis: int):
            if not s:
                return opened_parenthesis == 0

            if s[0] == '(':
                return match(s[1:], opened_parenthesis + 1)
            else:
                if s[0] == ')':
                    if opened_parenthesis > 0:
                        return match(s[1:], opened_parenthesis - 1)
                    else:
                        return False
                else:
                    return match(s[1:], opened_parenthesis + 1) \
                        or match(s[1:], opened_parenthesis) \
                        or (opened_parenthesis > 0 and match(s[1:], opened_parenthesis - 1))

        return match(s, 0)


if __name__ == '__main__':
    def test(s: str, expected: bool):
        assert Solution().checkValidString(s) == expected

    test('()', True)
    test('(*)', True)
    test('(*))', True)
