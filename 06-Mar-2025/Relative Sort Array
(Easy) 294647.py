# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_map = Counter(arr1)
        res = []

        for num in arr2:
            if num in arr1_map:
                res += [num] * arr1_map[num]
                del arr1_map[num]
        for num in sorted(arr1_map):
            res += [num] * arr1_map[num]
        return res