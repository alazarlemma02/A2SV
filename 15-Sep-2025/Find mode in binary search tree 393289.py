# Problem: Find mode in binary search tree - https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt_map = defaultdict(int)

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            cnt_map[node.val] +=1
            dfs(node.right)
        
        dfs(root)

        if not cnt_map: return []
        res = []
        max_fq = max(cnt_map.values())

        for elt in cnt_map:
            if cnt_map[elt] == max_fq:
                res.append(elt)
        return res
            