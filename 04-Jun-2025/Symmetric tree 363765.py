# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        qu_left = deque([root.left])
        qu_right = deque([root.right])

        while qu_left and qu_right:
            for i in range(len(qu_left)):
                cur_left = qu_left.popleft()
                cur_right = qu_right.popleft()
                
                if not cur_left and not cur_right:
                    continue
                if not cur_left or not cur_right:
                    return False
                if cur_left.val != cur_right.val:
                    return False
                
                qu_left.append(cur_left.left)
                qu_left.append(cur_left.right)
                qu_right.append(cur_right.right)              
                qu_right.append(cur_right.left)
            
        return True