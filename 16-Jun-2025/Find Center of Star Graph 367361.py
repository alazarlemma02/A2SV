# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_cnt = defaultdict(int)
        n = -1

        for edg in edges:
            n = max(n, edg[0])
            n = max(n, edg[1])
            edge_cnt[edg[0]] +=1
            edge_cnt[edg[1]] +=1

        for edg in edge_cnt:
            if edge_cnt[edg] == n-1:
                return edg