# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        max_ramp = -1
        dec_st = [0] * n

        i = n-1
        curr_max = nums[-1]
        while i >= 0:
            curr_max = max(curr_max, nums[i])
            dec_st[i] = curr_max
            i -=1
        
        left, right = 0, 1

        while right < n:
            if nums[left] > dec_st[right]:
                left +=1
            else:
                max_ramp = max(max_ramp, right - left)
                right +=1

        return max_ramp