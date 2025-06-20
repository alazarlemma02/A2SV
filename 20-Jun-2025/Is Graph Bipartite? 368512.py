# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node, curr_color):

            visited[node] = curr_color

            for ngh in graph[node]:
                if visited[ngh] == -1:
                    if not dfs(ngh, 1 - curr_color):
                        return False
                elif visited[ngh] == curr_color:
                    return False
                
            return True                

        visited = [-1] * len(graph)
        for i in range(len(graph)):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


        