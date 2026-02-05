#!/bin/python3
# https://leetcode.com/problems/


from typing import Dict, List, Optional, Tuple

type Edge = Tuple[int, float]


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        def build_map(conversions: List[List[int]]) -> Dict[int, List[Edge]]:
            conversion_map = {}
            for source_unit, target_unit, conversion_factor in conversions:
                if source_unit not in conversion_map:
                    conversion_map[source_unit] = []
                if target_unit not in conversion_map:
                    conversion_map[target_unit] = []
                conversion_map[source_unit].append((target_unit, conversion_factor))

            return conversion_map

        conversion_map = build_map(conversions)
        n = max(conversion_map.keys()) + 1
        result = [None] * n

        queue = [((0, 1), 1)]

        while queue:
            next_queue = []
            for conversion in queue:
                (unit, conversion_factor), from_zero_conversion_factor = conversion

                if result[unit] is None:
                    from_zero_conversion_factor *= conversion_factor
                    from_zero_conversion_factor %= 10**9 + 7
                    result[unit] = from_zero_conversion_factor

                    for conversion in conversion_map[unit]:
                        next_queue.append((conversion, from_zero_conversion_factor))

            queue = next_queue

        return result


if __name__ == "__main__":
    assert Solution().baseUnitConversions(
        [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 2], [4, 6, 3], [5, 7, 4]]
    ) == [1, 2, 3, 8, 10, 6, 30, 24]
