# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        holder = []

        def inorder(node, holder):
            if not node:
                return

            inorder(node.left, holder)
            holder.append(node.val)
            inorder(node.right, holder)

        inorder(root, holder)

        prev = holder[0]

        for i in range(1, len(holder)):
            if prev >= holder[i]:
                return False
            prev = holder[i]
        return True
        

    


                
