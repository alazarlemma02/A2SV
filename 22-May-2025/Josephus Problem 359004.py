# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

#Complete this function

class Solution:
    def josephus(self,n,k):
        #Your code here
        
        if n == 1:
            return 1
            
        return (self.josephus(n-1, k) + k-1) % n + 1