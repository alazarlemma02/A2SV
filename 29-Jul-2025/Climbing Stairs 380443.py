# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return n
        step_counter = [0] * (n+1)
        step_counter[1] = 1
        step_counter[2] = 2
        for i in range(3,n+1):
            step_counter[i] = step_counter[i-1] + step_counter[i-2]
        return step_counter[n]
            