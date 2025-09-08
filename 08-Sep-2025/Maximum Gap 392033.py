# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        x = sorted(nums)
        max_gap = 0
        n = len(x)
        for i in range(n-1):
            max_gap = max(max_gap, x[i+1]-x[i])
        return max_gap
        