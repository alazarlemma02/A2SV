# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """ 
        n = len(arr)

        total_zeros = arr.count(0)

        i, j = n-1, n + total_zeros - 1

        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            j -=1
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -=1
            i -=1  