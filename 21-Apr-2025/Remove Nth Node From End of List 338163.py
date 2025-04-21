# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next: return None
        left = right = head
        cnt = 1

        while right.next:
            cnt += 1
            right = right.next
        
        k = cnt - n

        if k <=0:
            head = head.next
            return head

        curr = 1

        while curr < k and left:
            curr +=1
            left = left.next
        
        if left.next.next is not None:
            left.next = left.next.next
        else:
            left.next = None
        return head