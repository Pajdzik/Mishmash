#!/bin/python3
# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rows = []

        rev1 = num1[::-1]
        rev2 = num2[::-1]

        for i, c1 in enumerate(rev1):
            row = [0 for _ in range(i)]
            overflow = 0
            d1 = int(c1)

            for c2 in rev2:
                d2 = int(c2)
                res = d1 * d2 + overflow
                row.append(res % 10)
                overflow = res // 10

            row.append(overflow)
            rows.append(row)

        reverse_sum = sum_rows(rows)
        reverse_product = reverse_sum[::-1]
        sum_str: str = ''.join(str(d) for d in reverse_product)

        no_leading_zeroes_sum_str = sum_str.lstrip('0')
        return no_leading_zeroes_sum_str if len(no_leading_zeroes_sum_str) > 0 else "0"


def sum_rows(rows: list[list[int]]):
    longest_row = max(len(row) for row in rows)
    row_sum = [0 for _ in range(longest_row + 1)]

    def add_with_overflow(index: int, sum: int):
        if sum == 0:
            return
        next_sum = row_sum[index] + sum
        row_sum[index] = (next_sum % 10)
        add_with_overflow(index + 1, next_sum // 10)

    for ci in range(longest_row):
        column_sum = sum([row[ci] if ci < len(row) else 0 for row in rows])
        add_with_overflow(ci, column_sum)

    return row_sum


if __name__ == "__main__":
    def test(expected: str, num1: str, num2: str):
        result = Solution().multiply(num1, num2)
        if expected != result:
            raise AssertionError(f'Expected {expected} was {result}')

    test("998001", "999", "999")
    test("0", "0", "0")
    test("56088", "123", "456")
