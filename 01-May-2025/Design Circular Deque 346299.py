# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        item = ListNode(value)
        if self.isFull():
            return False
        self.size -=1
        if self.isEmpty():
            self.head = self.tail = item
            item.next = item.prev = item
            return True
        item.next = self.head
        item.prev = self.tail
        self.head.prev = item
        self.tail.next = item
        self.head = item
        return True


    def insertLast(self, value: int) -> bool:
        item = ListNode(value)
        if self.isFull():
            return False
        self.size -=1
        if self.isEmpty():
            self.head = self.tail = item
            item.next = item.prev = item
            return True
        item.prev = self.tail
        self.tail.next = item
        self.tail = item
        self.tail.next = self.head
        self.head.prev = self.tail
        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.size +=1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return True
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size +=1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return True
        self.tail = self.tail.prev
        self.head.prev = self.tail
        self.tail.next = self.head
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.head is None        

    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()