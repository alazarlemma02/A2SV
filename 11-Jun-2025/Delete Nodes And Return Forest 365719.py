# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def traverse(node, fr):
            if not node:
                return

            node.left = traverse(node.left, fr)
            node.right = traverse(node.right, fr)

            if node.val in to_delete:
                if node.left:
                    fr.append(node.left)
                if node.right:
                    fr.append(node.right)
                return None
            else:
                return node
        
        fr = []

        remaining_root = traverse(root, fr)
        if remaining_root:
            fr.append(remaining_root)

        return fr