# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        uniq_nums = list(set(nums))
        uniq_nums.sort(reverse=True)

        if len(uniq_nums)<3:
            return uniq_nums[0]
        else:
            return uniq_nums[2]

        