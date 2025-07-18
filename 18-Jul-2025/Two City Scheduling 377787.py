# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        max_prof = []
        for i in range(n):
            diff = costs[i][0] - costs[i][1]
            heapq.heappush(max_prof, (diff, i))
        res = 0
        for i in range(n):
            prof, idx = heapq.heappop(max_prof)
            if i >= n//2:
                res += costs[idx][1]
            else:
                res += costs[idx][0]
        
        return res