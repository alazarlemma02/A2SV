# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, curr):
            if not node: return 0
            if not node.right and not node.left:
                curr.append(str(node.val))
                num = int("".join(curr))
                res.append(num)
                curr.pop()
                return

            curr.append(str(node.val))
            dfs(node.left, curr)
            dfs(node.right, curr)
            curr.pop()

        dfs(root, [])
        return sum(res)