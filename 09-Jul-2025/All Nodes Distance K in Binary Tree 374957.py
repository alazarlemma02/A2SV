# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def traverse(node):
            if not node: return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root)
 
        res = []
        qu = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)
        while qu:
            value, dist = qu.popleft()

            if dist == k:
                res.append(value)
            else:
                for ngh in graph[value]:
                    if ngh not in visited:
                        qu.append((ngh, dist+1))
                        visited.add(ngh)
        return res