# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def counter(new_k):
            if new_k < 0: return 0
            n = len(nums)

            i, nice_sub, curr = 0, 0, 0

            for j in range(n):
                if nums[j] % 2 != 0:
                    curr += 1
                
                while curr > new_k:
                    if nums[i] % 2 != 0:
                        curr -=1
                    i +=1
                
                nice_sub += j - i + 1

            return nice_sub

        return counter(k) - counter(k-1)