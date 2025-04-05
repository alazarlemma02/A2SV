# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_sum = 0

        i, curr_sum = 0, 0
        cnt_map = defaultdict(int)

        for j in range(n):
            curr_sum += nums[j]
            cnt_map[nums[j]] +=1
            
            if (j - i + 1) > k:
                curr_sum -= nums[i]
                cnt_map[nums[i]] -=1
                if cnt_map[nums[i]] == 0:
                    del cnt_map[nums[i]]
                i +=1

            if len(cnt_map) == k and (j - i + 1) == k:
                max_sum = max(max_sum, curr_sum)
 
        return max_sum
        