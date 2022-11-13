import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def calculate_distance(x, y):
            return x*x + y*y
        
        q = []
        
        for point in points:
            d = calculate_distance(*point)
            heapq.heappush(q, [d, point])

        return [p[1] for p in heapq.nsmallest(k, q, lambda x: x[0])]

if __name__ == "__main__":
    Solution().kClosest([[1,3],[-2,2],[2,-2]], 2)
    Solution().kClosest([[1,3],[-2,2]], 1)
    Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)