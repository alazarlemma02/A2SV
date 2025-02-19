# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        prev = set()
        while True:
            sum = 0
            while n!=0:
                sum += (n%10)**2
                n //= 10
            if sum == 1:
                return True
            n=sum
            if sum in prev:
                return False
            else:
                prev.add(sum)
        