# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        left, right = 0, n-1

        def insertion(left, right):
            if left > right:
                return

            mid = (right + left) // 2

            root = TreeNode(nums[mid])

            root.left = insertion(left, mid-1)
            root.right = insertion(mid+1, right)

            return root

        return insertion(left, right)