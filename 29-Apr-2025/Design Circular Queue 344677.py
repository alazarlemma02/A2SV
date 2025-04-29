# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = None
        self.tail = None
        
    def enQueue(self, value: int) -> bool:
        new_node = ListNode(value)
        if self.isFull():
            return False
        self.size -=1
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        return True   
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size +=1
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
            

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        if self.head == self.tail:
            return self.tail.val
        current = self.head
        while current.next != self.head:
            current = current.next
        return current.val      
        

    def isEmpty(self) -> bool:
        return self.head is None
        

    def isFull(self) -> bool:
        return self.size == 0
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()