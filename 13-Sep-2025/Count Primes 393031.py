# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        cnt_arr = [1] * n
        cnt_arr[0], cnt_arr[1] = 0, 0

        for i in range(2, n):
            if cnt_arr[i]:
                curr = i*2
                while curr < n:
                    cnt_arr[curr] = 0
                    curr += i
        return cnt_arr.count(1)
        