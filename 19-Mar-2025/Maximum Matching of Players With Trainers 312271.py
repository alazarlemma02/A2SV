# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        pn, tn = len(players), len(trainers)
        max_cnt = 0

        i, j = 0, 0

        players.sort()
        trainers.sort()

        while i < pn and j < tn:
            if players[i] <= trainers[j]:
                max_cnt +=1
                i += 1
            j +=1
        return max_cnt
