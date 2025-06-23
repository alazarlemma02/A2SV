# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        outgoing = set()
        incoming = set()
        for f, t in edges:
            outgoing.add(f)
            incoming.add(t)
            
        res = [v for v in outgoing if v not in incoming]
        return res

