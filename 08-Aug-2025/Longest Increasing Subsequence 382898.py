# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def dp(i, prev_index):
            if i == n:
                return 0
            
            if memo[i][prev_index] != -1:
                return memo[i][prev_index]
            
            not_take = dp(i + 1, prev_index)

            take = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                take = 1 + dp(i + 1, i)
            
            memo[i][prev_index] = max(take, not_take)
            return memo[i][prev_index]

        return dp(0, -1)
    
