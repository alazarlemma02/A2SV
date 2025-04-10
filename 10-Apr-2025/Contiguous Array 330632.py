# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        prx_sum, max_sub = 0, 0

        ocurr_map = {0:-1}

        for j in range(n):
            prx_sum += 1 if nums[j]==1 else -1
            if prx_sum not in ocurr_map:
                ocurr_map[prx_sum] = j
            if prx_sum in ocurr_map:
                res = j - ocurr_map[prx_sum]
                max_sub = max(max_sub, res)
        return max_sub