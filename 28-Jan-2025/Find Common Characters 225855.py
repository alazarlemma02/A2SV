# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        char_count = Counter(words[0])
        res = []
        for word in words:
            count = Counter(word)
            for ch in char_count:
                char_count[ch] = min(char_count[ch], count[ch])
        for char in char_count:
             if char_count[char] > 0:
                for i in range(char_count[char]):
                    res.append(char)
        return res

        