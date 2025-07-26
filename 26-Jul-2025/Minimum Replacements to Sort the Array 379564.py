# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        opts = 0
        prev = nums[-1]

        for idx in range(n - 2, -1, -1):
            curr = nums[idx]
            
            if curr <= prev:
                prev = nums[idx]
                continue
            curr_opt =ceil( curr /prev) 
            prev = curr // curr_opt
            
           
            
            opts += curr_opt - 1
        return opts