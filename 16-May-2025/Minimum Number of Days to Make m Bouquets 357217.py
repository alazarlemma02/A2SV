# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k: return -1

        def check(days):
            b_cnt, curr = 0, 0

            for bd in bloomDay:
                if bd <= days:
                    curr +=1
                else:
                    curr = 0
                
                if curr == k:
                    b_cnt += 1
                    curr = 0
                   
            return b_cnt

        left, right = 0, max(bloomDay)
        while left <= right:
            mid = (right + left)//2

            if check(mid) < m:
                left = mid + 1
            else:
                right = mid - 1
        return left

