# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2, l3 = [], [], ListNode()

        curr1, curr2 = l1, l2
        res = l3
        while curr1:
            st1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            st2.append(curr2.val)
            curr2 = curr2.next

        def addAtHead(val, head):
            new_node = ListNode(val)
            new_node.next = head.next
            head.next = new_node

        rem = 0
        while st1 or st2:
            curr = rem
            if st1:
                curr += st1[-1]
            if st2:
                curr += st2[-1]
            rem = curr//10
            ans = curr % 10
            addAtHead(ans, res)
            if st1: st1.pop()
            if st2: st2.pop()

        if rem !=0:
            addAtHead(rem,res)
        return l3.next