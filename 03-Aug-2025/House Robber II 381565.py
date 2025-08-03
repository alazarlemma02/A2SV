# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            n = len(nums)
            dp = [-1] * (n+1)

            def dfs(idx):
                if idx < 0:
                    return 0
                if idx == 0:
                    return nums[idx]
                if dp[idx] != -1:
                    return dp[idx]

                rob = nums[idx] + dfs(idx-2)
                notRob = dfs(idx-1)
                res = max(rob, notRob)
                dp[idx] = res
                return res

            return dfs(n-1) 
        return max(helper(nums[1:]), helper(nums[:-1]))