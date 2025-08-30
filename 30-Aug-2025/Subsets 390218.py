# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, nums, res, subset):
            
            if i == len(nums):
                res.append(list(subset))
                return
            
            subset.append(nums[i])
            dfs(i + 1, nums, res, subset)
            
            subset.pop()
            dfs(i + 1, nums, res, subset)

        subset = []
        nums.sort()
        res = []
        dfs(0, nums, res, subset)
        res.sort()
        return res