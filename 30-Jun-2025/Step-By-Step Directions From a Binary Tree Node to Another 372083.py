# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def dfs(node, target):
            if not node: return 

            if node.val == target:
                return ""

            left = dfs(node.left, target)
            if left is not None: 
                return "L" + left

            right = dfs(node.right, target)
            if right is not None: 
                return "R" + right

            return
        
        start_value_path = dfs(root, startValue)
        dest_value_path = dfs(root, destValue)

        i = 0
        n = min(len(start_value_path), len(dest_value_path))
        while i < n:
            if start_value_path[i] != dest_value_path[i]:
                break
            i +=1
        res = "U" * len(start_value_path[i:]) + dest_value_path[i:]
        return res