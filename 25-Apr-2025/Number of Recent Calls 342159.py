# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.recent_request = 0
        self.past_requests = deque()
        

    def ping(self, t: int) -> int:
        self.past_requests.append(t)
        curr_range = [t-3000, t]

        while self.past_requests and self.past_requests[0] < curr_range[0]:
            self.past_requests.popleft()
            self.recent_request -=1
        
        self.recent_request += 1
        return self.recent_request

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)