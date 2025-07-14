# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []
        for row in range(n):
            heapq.heappush(minHeap, (matrix[row][0], row, 0))

        while k:
            val, row, col = heapq.heappop(minHeap)
            if col + 1 < n:
                heapq.heappush(minHeap, (matrix[row][col+1], row, col+1))
            k -=1
        return val
