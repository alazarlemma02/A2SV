# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(cand, idx,target):
            if target == 0:
                res.append(cand)
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    break
                helper(cand + [candidates[i]], i, target - candidates[i])

            return

        helper([], 0, target)
        return res