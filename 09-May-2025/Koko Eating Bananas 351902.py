# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)

        while left < right:
            k = (right + left) // 2
            curr_hrs = 0
            for p in piles:
                curr_hrs += math.ceil(p/k)
            if curr_hrs <= h:
                right = k
            elif curr_hrs > h:
                left = k + 1
        return left
        