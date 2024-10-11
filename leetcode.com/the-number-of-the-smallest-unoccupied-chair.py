#!/bin/python3
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair

from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_times = sorted(times, key=lambda x: x[0])

        target_start_time, _ = times[targetFriend]
        chair_taken = [None for _ in range(len(times))]

        for start_time, end_time in sorted_times:
            for chair_index, chair_release_time in enumerate(chair_taken):
                # looking for the first unoccupied space
                if not (chair_release_time is None or chair_release_time <= start_time):
                    continue

                return_result = times[targetFriend][0] == start_time
                if return_result:
                    return chair_index

                chair_taken[chair_index] = end_time
                break

        return len(times) - 1


if __name__ == "__main__":

    def test(expected: int, times: List[List[int]], targetFriend: int):
        result = Solution().smallestChair(times, targetFriend)
        assert result == expected, f"{result = }, {expected = }"

    test(1, [[1, 4], [2, 3], [4, 6]], 1)

    test(
        5,
        [
            [18456, 68604],
            [56985, 77948],
            [78381, 93243],
            [994, 52805],
            [74055, 74713],
            [28046, 38437],
            [13144, 36471],
            [55010, 78071],
            [45167, 46100],
            [19329, 71693],
            [93343, 93345],
            [11898, 76052],
            [22636, 67509],
            [4161, 47678],
            [4993, 64796],
            [43618, 62684],
            [50633, 53488],
            [39027, 51820],
            [45852, 70938],
            [30220, 98399],
            [48716, 59269],
            [21594, 24359],
        ],
        0,
    )

    test(
        2,
        [
            [33889, 98676],
            [80071, 89737],
            [44118, 52565],
            [52992, 84310],
            [78492, 88209],
            [21695, 67063],
            [84622, 95452],
            [98048, 98856],
            [98411, 99433],
            [55333, 56548],
            [65375, 88566],
            [55011, 62821],
            [48548, 48656],
            [87396, 94825],
            [55273, 81868],
            [75629, 91467],
        ],
        6,
    )

    test(2, [[3, 10], [1, 5], [2, 6]], 0)
