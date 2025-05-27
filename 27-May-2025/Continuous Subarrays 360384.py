# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        left, cnt = 0, 0
        maxm, minm = float('-inf'), float('inf')

        for right in range(n):
            maxm = max(maxm, nums[right])
            minm = min(minm, nums[right])

            if maxm - minm > 2:
                size = right-left
                cnt += (size * (size+1))//2
                left = right

                minm, maxm = nums[right], nums[right]
                while abs(nums[right]-nums[left-1]) <= 2:
                    left -=1
                    maxm = max(maxm, nums[left])
                    minm = min(minm, nums[left])

                if left < right:
                    size = right - left
                    cnt -= (size * (size+1))//2

        size = n - left
        cnt += (size * (size+1))//2

        return cnt

            


        