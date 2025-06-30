# Problem: Clone Graph - https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = defaultdict(Node)

        def dfs(node):
            if not node: return

            if node in graph:
                return graph[node]

            dcopy = Node(node.val)
            graph[node] = dcopy

            for ngh in node.neighbors:
                dcopy.neighbors.append(dfs(ngh))
            return dcopy

        return dfs(node)
        