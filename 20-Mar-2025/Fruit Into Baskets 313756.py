# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_frt, cur_sum = 0, 0
        frt_map = defaultdict(int)

        i = 0

        for j in range(n):

            frt_map[fruits[j]] +=1
            cur_sum +=1

            while len(frt_map) > 2:
                frt_map[fruits[i]] -= 1
                cur_sum -=1
                if frt_map[fruits[i]] == 0:
                    del frt_map[fruits[i]]
                i +=1

            max_frt = max(max_frt, cur_sum)
        
        return max_frt