# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        current = ans
        prev = 0
        curr1, curr2 = l1, l2

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            curr = val1 + val2 + prev
            rem = curr % 10
            current.next = ListNode(rem)
            prev = curr // 10
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            current = current.next

        if prev != 0:
            current.next = ListNode(prev)
            
        return ans.next
