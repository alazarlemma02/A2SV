# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and n[-1] == k: return 1
        nums.sort()
        left, right, count = 0, n-1, 0

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == k:
                count +=1
                right -=1
                left +=1
            elif curr_sum > k:
                right -=1
            else:
                left +=1
        return count
        