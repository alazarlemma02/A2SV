# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(r1, r2):
            if not r1: return r2
            if not r2: return r1

            r1.val += r2.val
            r1.left = merge(r1.left, r2.left)
            r1.right = merge(r1.right, r2.right)

            return r1

        return merge(root1, root2)
        
        

        
        