#!/bin/python3
# https://leetcode.com/problems/basic-calculator

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        current_number = 0
        sign = 1
        store = []

        trimmed_s = s.replace(" ", "")
        for c in trimmed_s:
            if c.isdigit():
                current_number *= 10
                current_number += int(c)
            elif c == "+":
                result += sign * current_number

                current_number = 0
                sign = 1
            elif c == "-":
                result += sign * current_number

                current_number = 0
                sign = -1
            elif c == "(":
                store.append((sign, result))

                result = 0
                sign = 1
            elif c == ")":
                result += sign * current_number
                current_number = 0
                sign, previous_result = store.pop()
                result *= sign
                result += previous_result

                current_number = 0
                sign = 1

        result += sign * current_number
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.calculate("1-(     -2)") == 3
    assert solution.calculate("1 + 1") == 2
    assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert solution.calculate(" 2-1 + 2 ") == 3
