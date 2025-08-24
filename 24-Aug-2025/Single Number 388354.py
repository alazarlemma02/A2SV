# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
        