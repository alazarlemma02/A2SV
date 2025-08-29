# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0 for _ in range(n+1)]

        def find(i):
            while parent[i] != 0:
                i = find(parent[i])
            return i

        for edge in edges:
            px = find(edge[0])
            py = find(edge[1])

            if px == py:
                return edge
            parent[px] = py