# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nums_map = defaultdict(int)
        i, curr_sum, max_erasure = 0, 0, 0

        for j in range(n):

            if nums[j] in nums_map:
                while i <= nums_map[nums[j]]:
                    curr_sum -= nums[i]
                    i +=1
            
            nums_map[nums[j]] = j
            curr_sum += nums[j]

            max_erasure = max(max_erasure, curr_sum)

        return max_erasure

        