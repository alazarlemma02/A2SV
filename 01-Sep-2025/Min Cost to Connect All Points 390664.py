# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        total = 0

        while len(visited) < n:
            mnh_dis, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total += mnh_dis
            xi, yi = points[i]

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    ngh_dis = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (ngh_dis, j))

        return total