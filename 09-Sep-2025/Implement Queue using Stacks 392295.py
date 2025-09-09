# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.qu = deque()
        

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        temp = self.qu
        temp.reverse()
        res = temp.pop()
        temp.reverse()
        self.qu = temp
        return res

    def peek(self) -> int:
        return self.qu[0]
        

    def empty(self) -> bool:
        if not self.qu:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()