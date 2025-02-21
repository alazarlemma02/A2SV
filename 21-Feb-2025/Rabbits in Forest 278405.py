# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        MAP = Counter(answers)
        n = len(MAP)

        total = 0
        for k in MAP:
            if k == 0:
                total += MAP[k]
            elif MAP[k] == 1:
                total += k + 1
            else:
                if k+1 >= MAP[k]:
                    total += (k+1) * 1
                else:
                    c = ceil(MAP[k] / (k+1))
                    total += (k+1) * c
        return total


        

        