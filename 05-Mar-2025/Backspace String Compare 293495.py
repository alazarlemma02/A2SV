# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        s_list = []
        t_list = []
        for i in s:
            if i == "#":
              if s_list:
                s_list.pop()
            else:
              s_list.append(i)
        for j in t:
            if j == "#":
                if t_list:
                    t_list.pop()
            else:
              t_list.append(j)
        return s_list == t_list
        