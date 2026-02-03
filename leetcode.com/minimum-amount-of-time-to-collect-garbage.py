#!/bin/python3
# https://leetcode.com/problems/


from typing import Counter, List, Optional


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def get_total_travel_time(
            processsed_garbage: List[Counter[str]],
            type: str,
            cumulative_travel: List[int],
        ) -> int:
            filtered_garbage = [
                (i, el) for i, el in enumerate(processsed_garbage) if type in el
            ]

            if len(filtered_garbage) == 0:
                return 0

            collection_time = sum([c[type] for _, c in filtered_garbage])

            last_house = max([i for i, _ in filtered_garbage])
            travel_time = cumulative_travel[last_house]

            return collection_time + travel_time

        acc = 0
        cumulative_travel = [0]
        for el in travel:
            acc += el
            cumulative_travel.append(acc)

        processed_garbage = [Counter(s) for s in garbage]

        paper_time = get_total_travel_time(processed_garbage, "P", cumulative_travel)
        glass_time = get_total_travel_time(processed_garbage, "G", cumulative_travel)
        metal_time = get_total_travel_time(processed_garbage, "M", cumulative_travel)

        return paper_time + glass_time + metal_time


if __name__ == "__main__":
    assert Solution().garbageCollection(["MMM", "PGM", "GP"], [3, 10]) == 37
    assert Solution().garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]) == 21
