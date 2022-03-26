"""
This solution almost works, but not when there are duplicates...
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = self.inorder(root)
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                return False
        return True

    def inorder(self, root):
        if not root: return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

Actually it works after you put >= because apparently duplicates aren't allowed.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, floor=-float("inf"), ceil=float("inf")):
        return not root or root.val > floor and root.val < ceil and \
            self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceil)
