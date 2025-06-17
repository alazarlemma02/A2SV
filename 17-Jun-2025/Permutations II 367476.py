# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(p, up, res):
            if len(up) == 0:
                if p not in res:
                    res.append(p)
                return

            curr = up[0]
            for i in range(len(p)+1):
                dfs(p[0:i]+[curr]+p[i:], up[1:], res)

            return res

        return dfs([], nums, [])
