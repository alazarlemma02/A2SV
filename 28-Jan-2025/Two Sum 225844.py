# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        target_map = {}
        res = []
        for num in range(len(nums)):
            if target - nums[num] in target_map:
                res.append(target_map[target-nums[num]])
                res.append(num)
            if nums[num] not in target_map:
                target_map[nums[num]] = num
        return res
        