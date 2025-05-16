# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # even levels => odd nos str-increasing
        # odd levels => even nos str-decreasing

        qu = deque()
        even = True

        qu.append(root)

        while qu:
            prev = float("-inf") if even else float("inf")

            for n in range(len(qu)):
                curr = qu.popleft()

                if even:
                    if curr.val % 2 == 0 or curr.val <= prev:
                        return False                
                else:
                    if curr.val % 2 != 0 or curr.val >= prev:
                        return False
                
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
                
                prev = curr.val
                
            even = not even
        return True
