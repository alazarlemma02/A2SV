# Problem: Check Equal Arrays - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# User function Template for python3
from collections import defaultdict
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        a_map = defaultdict(int)
        b_map = defaultdict(int)
        
        for i in a:
            a_map[i] +=1
        for j in b:
            b_map[j] +=1
            
        return a_map == b_map