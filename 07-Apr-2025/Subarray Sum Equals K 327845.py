# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        cnt, prx_sum = 0, 0
        prx_map = {0:1}

        for num in nums:
            prx_sum += num

            cur = prx_sum - k
            if cur in prx_map:
                cnt += prx_map[cur]
            
            prx_map[prx_sum] = prx_map.get(prx_sum, 0) + 1

        return cnt
