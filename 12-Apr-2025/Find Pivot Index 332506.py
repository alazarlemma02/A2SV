# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prx_sum = 0

        for i in range(n):
            if prx_sum == (total - prx_sum - nums[i]):
                return i
            prx_sum += nums[i]
        return -1
        