# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)  
        nums.sort()
        max_streak, current_streak = 1, 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] +1 == nums[i+1]:
                current_streak +=1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        max_streak = max(max_streak, current_streak)
        return max_streak

        