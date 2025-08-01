# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(idx, curr_total):
            if idx < 0:
                if curr_total == target:
                    return 1
                return 0
            if (idx, curr_total) in memo:
                return memo[(idx, curr_total)]
            cnt = dfs(idx-1, curr_total + nums[idx]) + dfs(idx-1, curr_total - nums[idx])

            memo[(idx, curr_total)] = cnt
            
            return cnt
        
        return dfs(n-1, 0)