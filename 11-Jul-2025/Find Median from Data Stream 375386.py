# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.maxHeap = []  
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -1 * num)

        if self.maxHeap and self.minHeap and (
            -1*self.maxHeap[0] > self.minHeap[0]):
            val = -1*(heappop(self.maxHeap))
            heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1*(heappop(self.maxHeap))
            heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -1*val)
        

    def findMedian(self) -> float:
        minLen, maxLen = len(self.minHeap), len(self.maxHeap)
        if maxLen > minLen:
            return -1*self.maxHeap[0]
        elif minLen > maxLen:
            return self.minHeap[0]
        else:
            return (-1*self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()