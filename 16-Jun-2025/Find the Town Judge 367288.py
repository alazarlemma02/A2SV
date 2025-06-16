# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_edges = defaultdict(int)
        outgoing_edges = defaultdict(int)

        for t in trust:
            incoming_edges[t[1]] +=1
            outgoing_edges[t[0]] +=1

        for i in range(1, n+1):
            if incoming_edges[i] == n-1 and outgoing_edges[i] == 0:
                return i
        return -1
        