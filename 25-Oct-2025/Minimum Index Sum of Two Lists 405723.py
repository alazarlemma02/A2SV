# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        cnt_map = defaultdict(int)
        res = []
        total = float('inf')

        for i in range(len(list1)):
            cnt_map[list1[i]] = i
        print(cnt_map)

        for j in range(len(list2)):
            if list2[j] in cnt_map:
                curr = cnt_map[list2[j]] + j
                if curr < total:
                    res = []
                    res.append(list2[j])
                    total = curr
                elif curr == total:
                    res.append(list2[j])
        return res



        