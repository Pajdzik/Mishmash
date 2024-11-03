#!/bin/python3
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank

from typing import Counter, List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        def count_ones(index: str) -> int:
            c = Counter(bank[index])
            return c.get("1", 0)

        def find_next_row(row: int) -> tuple[int, int]:
            while row < len(bank):
                count = count_ones(row)
                if count > 0:
                    return [row, count]

                row += 1

            return [-1, -1]

        result = 0
        current_row, current_row_count = find_next_row(0)

        while True:
            current_row, next_row_count = find_next_row(current_row + 1)
            if current_row == -1:
                break

            result += current_row_count * next_row_count
            current_row_count = next_row_count

        return result


def main():
    solution = Solution()

    # Test cases
    bank1 = ["011001", "000000", "010100", "001000"]
    assert (
        solution.numberOfBeams(bank1) == 8
    ), f"Test case 1 failed: {solution.numberOfBeams(bank1)}"

    bank2 = ["000", "111", "000"]
    assert (
        solution.numberOfBeams(bank2) == 0
    ), f"Test case 2 failed: {solution.numberOfBeams(bank2)}"

    bank3 = ["101", "000", "101"]
    assert (
        solution.numberOfBeams(bank3) == 1
    ), f"Test case 3 failed: {solution.numberOfBeams(bank3)}"

    bank4 = ["1", "0", "1"]
    assert (
        solution.numberOfBeams(bank4) == 1
    ), f"Test case 4 failed: {solution.numberOfBeams(bank4)}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
