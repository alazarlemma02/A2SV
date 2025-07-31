# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0: return cost[0]
        if n == 1: return min(cost[0], cost[1])

        i, j = cost[0], cost[1]

        for c in cost[2:]:
            curr = min(i, j) + c
            i = j
            j = curr
        return min(i, j)