# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        min_len = float('inf')
        i= 0
        curr_sum = 0

        for j in range(n):
            curr_sum += nums[j]

            while curr_sum >= target:
                curr_sum -= nums[i]
                min_len = min(min_len, j - i + 1)
                i +=1
                
        if min_len == float('inf'):
            return 0
        return min_len