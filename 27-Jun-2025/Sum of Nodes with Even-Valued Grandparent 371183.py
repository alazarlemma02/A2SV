# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def dfs(node, parent, g_parent):
            if not node: return 0
            res = 0
            if g_parent and g_parent % 2 == 0:
                res +=node.val

            res +=dfs(node.left, node.val, parent)
            res +=dfs(node.right, node.val, parent)

            return res
        return dfs(root, None, None)