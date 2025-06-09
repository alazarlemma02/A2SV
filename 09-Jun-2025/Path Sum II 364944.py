# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res, st, cur = [], [], 0

        def traverse(node, res, st, cur):
            if not node:
                return []

            st.append(node.val)
            cur += node.val
            if not node.left and not node.right and cur == targetSum:
                res.append(st[:])
                
            traverse(node.left, res, st, cur)
            traverse(node.right, res, st, cur)

            st.pop()            

        traverse(root, res, st, cur)
        return res 
            