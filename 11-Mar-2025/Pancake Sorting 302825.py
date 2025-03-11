# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr): return []

        res = []
        n = len(arr)

        while n > 1:
            idx = arr.index(max(arr[:n]))

            if idx != 0:
                res.append(idx+1)
                arr[:idx+1] = arr[:idx+1][::-1]

            arr[:n] = arr[:n][::-1]
            res.append(n)
            n -=1
        return res


        