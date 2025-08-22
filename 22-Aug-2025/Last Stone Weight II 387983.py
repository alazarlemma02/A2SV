# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        n = len(stones)
        targ = ceil(stone_sum / 2)

        memo = {}
        def dfs(idx, total):
            if total >= targ or idx == n:
                return abs(total - (stone_sum - total))
            if (idx, total) in memo:
                return memo[(idx, total)]
            
            memo[(idx, total)] = min(dfs(idx+1, total), 
                dfs(idx+1, total+stones[idx]))
            return memo[(idx, total)]

        return dfs(0, 0)