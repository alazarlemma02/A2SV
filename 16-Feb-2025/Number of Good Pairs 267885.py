# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        result = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    result += 1
        return result
        