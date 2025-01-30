# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = sorted(strs)
        res = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res += strs[0][i]
            else:
                return res
        return res
        