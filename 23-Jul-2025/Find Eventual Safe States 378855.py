# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]: 
        n = len(graph)
        visited = [0] * n

        def dfs(node):
            if visited[node] != 0:
                return visited[node] == 2
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True
        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res