# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):

        MAP = {}
        for name, height in zip(names, heights):
            MAP[height] = name
        
        result = [MAP[height] for height in sorted(MAP, reverse=True)]
        return result
        

        
        