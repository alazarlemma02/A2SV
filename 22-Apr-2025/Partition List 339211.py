# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        less, greater = ListNode(), ListNode()
        l, g = less, greater

        while head:
            if head.val >= x:
                g.next = head
                g = g.next
            else:
                l.next = head
                l = l.next
            head = head.next
        g.next = None
        l.next = greater.next
        return less.next

        