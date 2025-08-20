# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(target):
            if target == 0:
                return 1
            if target in memo:
                return memo[target]

            cnt = 0
            for num in nums:
                if num <= target:
                    cnt += dfs(target-num)
            memo[target] = cnt
            return memo[target]

        return dfs(target)
        