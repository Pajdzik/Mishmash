import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extra_students: int) -> float:
        classes_with_ratios = [
            [-(((c[0] + 1) / (c[1] + 1)) - c[0] / c[1]), c[0] / c[1], c[0], c[1]]
            for c in classes
        ]

        heapq.heapify(classes_with_ratios)

        while extra_students > 0:
            [_, _, pss, tot] = heapq.heappop(classes_with_ratios)
            ratio = (pss + 1) / (tot + 1)
            next_ratio = (pss + 2) / (tot + 2)
            heapq.heappush(
                classes_with_ratios,
                [-(next_ratio - ratio), ratio, pss + 1, tot + 1],
            )
            extra_students -= 1

        sum_ratio = sum([x[1] for x in classes_with_ratios])
        return sum_ratio / len(classes)


if __name__ == "__main__":
    Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)
    Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4)
