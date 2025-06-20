# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(node):
            res = True

            visited[node] = 2

            for ngh in graph[node]:
                if visited[ngh] == 2:
                    return False
                if not visited[ngh]:
                    res = res and dfs(ngh)

            visited[node] = 1
            return res
            
        visited = [0]*numCourses
        res = True
        for i in range(numCourses):
            if not visited[i]:
                res = res and dfs(i)
        return res
