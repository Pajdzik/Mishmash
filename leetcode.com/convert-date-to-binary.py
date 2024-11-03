#!/bin/python3
# https://leetcode.com/problems/convert-date-to-binary


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts = [int(x) for x in date.split("-")]
        bin_parts = [bin(x)[2:] for x in parts]
        return "-".join(bin_parts)


def main():
    solution = Solution()
    assert solution.convertDateToBinary("2023-10-05") == "11111100111-1010-101"
    assert solution.convertDateToBinary("1990-01-01") == "11111000110-1-1"
    assert solution.convertDateToBinary("2000-12-31") == "11111010000-1100-11111"


if __name__ == "__main__":
    main()
