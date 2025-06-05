# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        qu = deque([root])

        while qu:
            for i in range(len(qu)):
                curr = qu.popleft()

                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
            res.append(curr.val)
        return res

        
                     
        