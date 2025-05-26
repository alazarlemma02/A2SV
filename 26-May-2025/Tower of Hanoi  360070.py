# Problem: Tower of Hanoi  - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

# User function Template for python3

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        
        # f -> t -> a  n-1
        # f -> a -> t  1
        # a -> f -> t  n-1
        if n == 0:
            return 0
            
        moves_cnt = 0
        
        moves_cnt += self.towerOfHanoi(n-1, fromm, aux, to)
        moves_cnt +=1
        moves_cnt += self.towerOfHanoi(n-1, aux, to, fromm)
        
        return moves_cnt