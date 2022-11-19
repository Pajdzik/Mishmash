#!/bin/python3
# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        conditions = [[] for _ in range(numCourses)]

        for course, condition in prerequisites:
            if course == condition:
                return False
            conditions[course].append(condition)

        visited = [False] * numCourses
        for course in range(numCourses):
            if self.has_cycle(course, conditions, visited):
                return False
            
        return True
    
    def has_cycle(self, course: int, conditions: list[list[int]], visited: list[bool]):
        if visited[course]:
            return True
        
        visited[course] = True
        cycle = False

        for condition in conditions[course]:
            cycle = self.has_cycle(condition, conditions, visited)
            if cycle:
                break

        visited[course] = False
        
        return cycle

if __name__ == "__main__":
    assert(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
    # assert(Solution().canFinish(2, [[1,0]]))
    # assert(not Solution().canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
    # assert(not Solution().canFinish(2, [[1,0],[0,1]]))