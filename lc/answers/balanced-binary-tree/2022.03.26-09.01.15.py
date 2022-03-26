"""
naive way...

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

Let's see if we can get to O(n)
we just need to get the height of every node and make comparisons
on the way back up
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.recurse(root)
        return False if res is None else True

    def recurse(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.recurse(root.left)
        right = self.recurse(root.right)
        if left is None or right is None or abs(left - right) > 1:
            return None
        return max(left, right) + 1









