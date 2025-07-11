# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        maxHeap = []
        for num in nums_map:
            heapq.heappush(maxHeap, (-1*nums_map[num], num))

        res = []
        for _ in range(k):
            freq, num = heapq.heappop(maxHeap)
            res.append(num)
        return res

