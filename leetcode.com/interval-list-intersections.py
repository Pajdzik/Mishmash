#!/bin/python3
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
        result = []
        first = 0
        second = 0

        while first < len(first_list) and second < len(second_list):
            start = max(first_list[first][0], second_list[second][0])
            end = min(first_list[first][1], second_list[second][1])

            if start <= end:
                result.append([start, end])

            if first_list[first][1] <= second_list[second][1]:
                first += 1
            else:
                second += 1

        return result

    def overlap(self, first_interval: list[int], second_interval: list[int]) -> bool:
        if first_interval[0] <= second_interval[0] <= first_interval[1]:
            return True

        if second_interval[0] <= first_interval[0] <= second_interval[1]:
            return True

        return False

    def intervalIntersection_bf(self, first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
        result = []
        first = 0
        second = 0

        while first < len(first_list):
            while second < len(second_list) and first_list[first][1] >= second_list[second][0]:
                if self.overlap(first_list[first], second_list[second]):
                    result.append([max(first_list[first][0], second_list[second][0]), min(first_list[first][1], second_list[second][1])])
                
                second += 1

            first += 1
            second = 0

        return result
            
            

Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])
