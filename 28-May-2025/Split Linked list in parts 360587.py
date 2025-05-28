# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_len = 0
        curr = head
        while curr:
            total_len += 1
            curr = curr.next

        part_size = total_len // k
        extra_nodes = total_len % k 

        result = []
        curr = head
        for i in range(k):
            part_head = curr
            size = part_size + (1 if i < extra_nodes else 0)

            for j in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part_head)
        return result
