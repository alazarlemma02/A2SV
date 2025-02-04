# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution(object):
    def buildArray(self, nums):
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans
        