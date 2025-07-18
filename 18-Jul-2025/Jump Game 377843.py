# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i, last = n-1, n-1
        while i >=0:
            if i + nums[i] >= last:
                last = i
            i -= 1
        return True if last == 0 else False