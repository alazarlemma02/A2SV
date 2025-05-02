# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 1
        current = head
        while current.next:
            n +=1
            current = current.next

        st, max_twin, count = [], 0, n/2
        current = head
        while current:
            if count == 0:
                max_twin = max(max_twin, st[-1]+current.val)
                st.pop()
            else:
                count -=1
                st.append(current.val)
            current = current.next

        return max_twin
        