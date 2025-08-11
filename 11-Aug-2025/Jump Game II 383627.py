# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            curr_min = float('inf')
            for j in range(i):
                if j + nums[j] >= i:
                    curr_min = min(curr_min, dp[j]+1)
            dp[i] = curr_min
        return dp[-1]