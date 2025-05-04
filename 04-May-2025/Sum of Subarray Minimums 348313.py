# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        res = 0        
        stack = []
        prev_less = [-1] * n
        next_less = [n] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        for i in range(n):
            left_cnt = i - prev_less[i]
            right_cnt = next_less[i] - i
            res = (res + arr[i] * left_cnt * right_cnt) % MOD

        return res