# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        smap = defaultdict(str)
        res = []
        
        for sen in s.split():
            smap[int(sen[-1])] = sen[:-1]

        for i in range(len(smap)):
            res.append(smap[i+1])
        return " ".join(res)  