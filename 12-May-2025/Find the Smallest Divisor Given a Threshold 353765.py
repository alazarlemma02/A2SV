# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if n == threshold: return max(nums)
        nums.sort()
        
        left, right = 1, max(nums)
        divisor = 0

        while left <= right:
            mid = (right + left) // 2
            
            curr, i = 0, n-1
            while i >= 0 and nums[i] > mid:
                curr += ceil(nums[i] / mid)
                i -=1
            curr += i + 1

            if curr <= threshold:
                divisor = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return divisor



