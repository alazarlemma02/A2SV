# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        def traverse(node, l):
            if not node: 
                l.append(None)
                return

            traverse(node.left, l)
            traverse(node.right, l)
            l.append(node.val)

        traverse(p, r1)
        traverse(q, r2)
        return r1 == r2
        