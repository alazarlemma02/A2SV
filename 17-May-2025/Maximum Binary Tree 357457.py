# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def create(nums):
            if not nums: return

            max_no = max(nums)
            idx = nums.index(max_no)

            root = TreeNode(max_no)
            root.left = create(nums[:idx])
            root.right = create(nums[idx+1:])

            return root

        return create(nums)