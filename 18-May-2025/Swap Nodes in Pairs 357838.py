# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy

        while current.next and current.next.next:
            adj_1 = current.next
            adj_2 = adj_1.next

            adj_1.next = adj_2.next
            adj_2.next = adj_1

            current.next = adj_2
            current = adj_1
        return dummy.next
        
        