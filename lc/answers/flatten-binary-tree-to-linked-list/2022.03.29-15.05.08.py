"""
read this one about 'reverse preorder'
preorder is curr left right
reversed is right left curr
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def recurse(node):
            nonlocal prev
            if node:
                recurse(node.right)
                recurse(node.left)
                node.right = prev
                node.left = None
                prev = node
        recurse(root)
        return root