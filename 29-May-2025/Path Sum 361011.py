# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node, total):
            if not node:
                return False

            total += node.val
            if not node.left and not node.right:
                return total == targetSum

            return traverse(node.left, total) or traverse(node.right, total)
            

        return traverse(root, 0)