# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        i, chance, max_sub = 0, 0, 0

        for j in range(n):
            if nums[j] == 0:
                chance +=1

            while chance > 1:
                if nums[i] == 0:
                    chance -=1
                i +=1
            max_sub = max(max_sub, j - i)

        return max_sub