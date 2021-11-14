#!/bin/python3
# https://leetcode.com/problems/decode-string/

from typing import Tuple

class Solution:
    def decodeString(self, s: str) -> str:
        def load_number(s: str, index: int) -> Tuple[int, int]:
            number = 0
            while s[index].isdigit():
                number *= 10
                number += int(s[index])
                index += 1

            return number, index

        def decode(s: str, index: int) -> str:
            if index >= len(s):
                return ""

            result = []

            while index < len(s):
                if s[index] == ']':
                    return (''.join(result), index)
                elif s[index].isdigit():
                    times, index = load_number(s, index)
                    nested_result, index = decode(s, index + 1)
                    result.append(times * nested_result)
                elif s[index] == '[':
                    pass
                else:
                    result.append(s[index])

                index += 1

            return (''.join(result), index + 1)

        result, _ = decode(s, 0)
        return result

if __name__ == "__main__":
    assert(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
    assert(Solution().decodeString("100[leetcode]") == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")
    assert(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
    assert(Solution().decodeString("3[a2[c]]") == "accaccacc")