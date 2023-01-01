# https://leetcode.com/problems/course-schedule/description/
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = { i:[] for i in range(numCourses) }
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        indegree = [0] * numCourses
        for i in range(numCourses):
            for it in graph[i]:
                indegree[it] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            
            for it in graph[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    queue.append(it)
        if count == numCourses:
            return True    
        return False