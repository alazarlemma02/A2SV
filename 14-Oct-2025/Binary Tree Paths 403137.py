# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def traverse(node, temp):
            if not node: return

            temp.append(str(node.val))

            if not node.left and not node.right:
                res.append("->".join(temp)) 
            else:            
                traverse(node.left, temp[:])
                traverse(node.right, temp[:])
            
            return res

        traverse(root, [])
        return res
