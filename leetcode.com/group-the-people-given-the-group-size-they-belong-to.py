#!/bin/python3
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        group_size_to_indices: dict[int, list[int]] = {}

        for i, group_size in enumerate(groupSizes):
            if not group_size in group_size_to_indices:
                group_size_to_indices[group_size] = []

            group_size_to_indices[group_size].append(i)

        result = []

        for group_size in group_size_to_indices:
            indices = group_size_to_indices[group_size]

            for start_index in range(0, len(indices), group_size):
                result.append(indices[start_index : start_index + group_size])

        return result


if __name__ == "__main__":

    def test(value: list[int], expected: list[list[int]]):
        s = Solution()
        result = s.groupThePeople(value)
        assert result == expected, f"For {value}, expected {expected} but got {result}"

    test([3, 3, 3, 3, 3, 1, 3], [[5], [0, 1, 2], [3, 4, 6]])
