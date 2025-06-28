# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return []
        queue = deque([root])
        deepest_node = []
        while queue:
            curr_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_level.append(curr)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            deepest_node = curr_level
        

        def dfs(node, p, q):
            if not node or node in [p, q]:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if not left: return right
            if not right: return left
            else: return node

        p, q = deepest_node[0], deepest_node[-1]
        return dfs(root, p, q)
                

        