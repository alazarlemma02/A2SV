# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for num in range(len(nums)-2):
            l, r = num+1, len(nums)-1
            while l < r:
                total = nums[num] + nums[l] + nums[r]
                if  total == 0 and [nums[num], nums[l], nums[r]] not in res:
                    res.append([nums[num], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
        