# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        max_sum = (n * (n+1)) / 2 # formula to find sum of [0, n] digits
        return max_sum - sum(nums)

        