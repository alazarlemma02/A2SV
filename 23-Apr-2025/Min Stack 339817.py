# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.head = ListNode()
        self.min_cntr = [float('inf')]

    def push(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node
        if self.min_cntr[-1] >= new_node.val:
            self.min_cntr.append(new_node.val)

    def pop(self) -> None:
        if self.head is None: return
        poped_node = self.head
        self.head = self.head.next
        poped_node.next = None
        if poped_node.val == self.min_cntr[-1]:
            self.min_cntr.pop()

    def top(self) -> int:
        if self.head is None: return
        return self.head.val
        
    def getMin(self) -> int:
        return self.min_cntr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()