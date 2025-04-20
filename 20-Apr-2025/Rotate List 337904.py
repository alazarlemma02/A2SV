# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            length += 1
            current = current.next
        
        current.next = head

        k = k % length
        new_tail = length - k

        temp, count = head, 0

        while count < new_tail-1:
            temp = temp.next
            count +=1
        
        new_head = temp.next
        temp.next = None

        return new_head