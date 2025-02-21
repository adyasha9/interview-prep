# Course Schedule II
# You are given an array prerequisites where prerequisites[i] = [a, b] 
# indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses.
#  If there are many valid answers, return any of them. 
# If it's not possible to finish all courses, return an empty array.

# Example 1:

# Input: numCourses = 3, prerequisites = [[1,0]]

# Output: [0,1,2]
# Explanation: We must ensure that course 0 is taken before course 1.

# Example 2:

# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

# Output: []

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()
        visiting = set()
        res = []
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            neighbors = graph[course]
            for nei in neighbors:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res