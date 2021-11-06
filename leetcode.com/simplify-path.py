#!/bin/python3
# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for el in path.split('/'):
            if el == '.':
                continue
            elif el == '..':
                if stack:
                    stack.pop()
            elif el == '':
                continue
            else:
                stack.append(el)

        if stack:
            result = []
            for el in stack:
                result.append('/')
                result.append(el)

            result = ''.join(result)
            return result
        else:
            return "/"

if __name__ == "__main__":
    assert(Solution().simplifyPath("/home/") == "/home")
    assert(Solution().simplifyPath("/home//foo/") == "/home/foo")
    assert(Solution().simplifyPath("/a/./b/../../c/") == "/c")