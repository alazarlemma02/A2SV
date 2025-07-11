# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [-x for x in piles]
        heapq.heapify(piles)

        for _ in range(k):
            curr = heapq.heappop(piles)
            total += curr
            val = ceil((-1*curr)/2)
            total += val
            heapq.heappush(piles, -1*val)
        return total

        