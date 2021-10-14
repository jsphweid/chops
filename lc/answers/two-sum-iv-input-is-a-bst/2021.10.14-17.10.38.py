"""
===== Initial Thoughts =====
so we can look for items on a loop... ie. traverse the tree each node at a time, and at each node look
for a compliment. but a faster way would seem to just traverse the whole thing looking for compliments
at the same time
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        found_nums = set()
        def recurse(node):
            if not node: return False
            compliment = k - node.val
            if compliment in found_nums: return True
            found_nums.add(node.val)
            return recurse(node.left) or recurse(node.right)
        return recurse(root)