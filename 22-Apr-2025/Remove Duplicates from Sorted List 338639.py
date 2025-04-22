# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(val=None)
        prev.next = head
        current = head

        while current:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head
                
        