# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        smallest = root.val
        smallest_diff = abs(root.val - target)
        def recurse(node):
            nonlocal smallest
            nonlocal smallest_diff
            diff = abs(node.val - target)
            if diff < smallest_diff:
                smallest = node.val
                smallest_diff = diff
            if node.left: recurse(node.left)
            if node.right: recurse(node.right)
        recurse(root)
        return smallest