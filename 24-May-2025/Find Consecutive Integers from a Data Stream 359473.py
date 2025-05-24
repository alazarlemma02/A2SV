# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.its = deque()
        self.value, self.k = value, k
        

    def consec(self, num: int) -> bool:
        while self.its and self.its[-1] != num:
            self.its.popleft()
        
        if num == self.value:
            self.its.append(num)

        if len(self.its) >= self.k:
            return True

        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)