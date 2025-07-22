# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        res = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] +=1
            
        qu = deque()
        for i, c in enumerate(indegrees):
            if c == 0:
                qu.append(i)
        
        while qu:
            curr = qu.popleft()
            res.append(curr)
            for ngh in graph[curr]:
                indegrees[ngh] -=1
                if not indegrees[ngh]:
                    qu.append(ngh)
        return [] if len(res) != numCourses else res
