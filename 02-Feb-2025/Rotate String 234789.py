# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)
        current = 0

        while current < n:
            s += s[current]
            if s[current+1:]==goal:
                return True 
            current +=1
        return False
        