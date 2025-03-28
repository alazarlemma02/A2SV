# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_sum = 0
        pref_map = {0:-1}
        
        for i in range(n):
            prefix_sum += nums[i]
            rem = prefix_sum % k
            if rem in pref_map:
                prev_idx = pref_map[rem]
                if i - prev_idx >= 2:
                    return True
            else:
                pref_map[rem] = i
        return False