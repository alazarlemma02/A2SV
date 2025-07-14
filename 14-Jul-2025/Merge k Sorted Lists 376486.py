# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        n = len(lists)
        minHeap = []
        
        for r in range(n):
            current = lists[r]
            while current:
                heapq.heappush(minHeap, current.val)
                current = current.next

        res = ListNode(-1)
        current = res
        while minHeap:
            curr = ListNode(heapq.heappop(minHeap))
            current.next = curr
            current = current.next

        return res.next
        