# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res

        qu = deque([root])
        st = []
        even = True

        while qu:
            r = []
            
            for _ in range(len(qu)):
                curr = qu.popleft()

                if even:
                    r.append(curr.val)
                else:
                    st.append(curr.val)

                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)     
            
            while st:
                r.append(st.pop())
            
            even = not even
          
            res.append(r)
        return res
        