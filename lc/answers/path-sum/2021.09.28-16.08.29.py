# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        if remaining == 0 and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, remaining)
        right = self.hasPathSum(root.right, remaining)
        return any([left, right])