# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        st = deque()
        count = 0

        for i in range(len(tickets)):
            st.append(i)

        while tickets[k] != 0:
            if len(st) == 1:
                return count + tickets[st[0]]
            curr = tickets[st[0]] -1
            tickets[st[0]] = curr
            if curr !=0:
                st.append(st[0])
            st.popleft()
            count +=1
        return count