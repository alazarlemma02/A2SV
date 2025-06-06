# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def traverse(node, order):
            if not node:
                return
            
            traverse(node.left, order)
            order.append(node.val)
            traverse(node.right, order)
        
        traverse(root, order)
        return order[k-1]
        