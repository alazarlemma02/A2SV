# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        MAP = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in MAP:
                MAP[ss] +=[s]
            else:
                MAP[ss]=[s]
        return [MAP[key] for key in MAP]