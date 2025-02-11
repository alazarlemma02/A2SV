# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dynamic_list = [nums[0], max(nums[0],nums[1])]
        while len(dynamic_list) < len(nums):
            n = len(dynamic_list)
            total_money = max(
                dynamic_list[n-2] + nums[n],
                dynamic_list[n-1]
            )
            dynamic_list.append(total_money)
        return dynamic_list[-1]

        