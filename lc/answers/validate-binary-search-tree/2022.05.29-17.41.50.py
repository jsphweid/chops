# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return (True, None, None)
            if not node.left and not node.right:
                return (True, node.val, node.val)
            l_valid, l_lo, l_hi = helper(node.left)
            r_valid, r_lo, r_hi = helper(node.right)
            if l_valid is False or r_valid is False:
                return (False, None, None)
            if l_hi and l_hi >= node.val:
                return (False, None, None)
            if r_lo and r_lo <= node.val:
                return (False, None, None)
            lo = l_lo or node.val
            hi = r_hi or node.val
            return (True, lo, hi)
        return helper(root)[0]