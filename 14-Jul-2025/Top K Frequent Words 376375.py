# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_map = Counter(words)
        heap = []
        res = []
        for num in words_map:
            heapq.heappush(heap, (-1*words_map[num], num))
        for _ in range(k):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res
       


        