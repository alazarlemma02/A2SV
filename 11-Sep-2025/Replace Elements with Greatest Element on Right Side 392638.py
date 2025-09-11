# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elt = arr[-1]
        arr[-1] = -1

        i = len(arr)-2
        while i >= 0:
            curr = arr[i]
            arr[i] = max_elt
            max_elt = max(max_elt, curr)
            i -= 1
        return arr
        