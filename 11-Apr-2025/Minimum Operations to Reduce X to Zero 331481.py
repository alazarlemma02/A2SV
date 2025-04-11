# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        i, curr_sum, total, min_opp = 0, 0, sum(nums), float('inf')

        if total < x:
            return -1

        for j in range(n):
            curr_sum += nums[j]

            while total - curr_sum < x:
                curr_sum -= nums[i]
                i += 1

            if total - curr_sum == x:
                min_opp = min(min_opp, n - (j - i + 1))
        
        return -1 if min_opp == float('inf') else min_opp