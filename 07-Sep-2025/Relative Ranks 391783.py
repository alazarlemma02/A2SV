# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution(object):
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)
        score_map = {}
        place = 0
        for s in sorted_score:
            place+=1
            score_map[s]= place
        res = []
        for s in range(len(score)):
            if score_map[score[s]]==1:
                res.append( "Gold Medal")
            elif score_map[score[s]]==2:
                res.append("Silver Medal")
            elif score_map[score[s]]==3:
                res.append("Bronze Medal")
            else:
                res.append(str(score_map[score[s]]))
        return res