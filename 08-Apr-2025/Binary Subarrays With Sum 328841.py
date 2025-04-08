# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def counter(new_goal):
            if new_goal < 0: return 0
            n = len(nums)

            i, cnt, cur = 0, 0, 0

            for j in range(n):
                cur += nums[j]

                while cur > new_goal:
                    cur -= nums[i]
                    i +=1
                
                cnt += j - i + 1
            return cnt
        
        return counter(goal) - counter(goal-1)
            