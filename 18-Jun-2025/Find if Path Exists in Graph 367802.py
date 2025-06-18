# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for ngh in graph[node]:
                if ngh not in visited:
                    if dfs(ngh):
                        return True
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(source)
        return dfs(source)