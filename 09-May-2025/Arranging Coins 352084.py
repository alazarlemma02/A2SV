# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (right + left) // 2
            rows = (mid*(mid+1)) // 2
            if rows == n:
                return mid
            elif rows < n:
                left = mid + 1
            else:
                right = mid - 1
        return right