# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left, right = 1, 2**(n-1)
        i, val = 0, 0

        while i <= n-1:
            mid = (right + left) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                val = 0 if val else 1
            i +=1
        return val

            