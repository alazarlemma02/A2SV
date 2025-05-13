# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depthTrav(node, depth):
            if not node:
                return depth

            return max(
                depthTrav(node.left, depth+1), 
                depthTrav(node.right, depth+1)
                )
            
        return depthTrav(root, 0)