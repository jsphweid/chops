"""
We somehow need to traverse the entire graph but only return left leaf sums

maybe we could recurse and return all leaf values to be added but at some high level we change it
to 0 if it's a right leaf.

somehow top level node by itself can't have a sum

left_sum = root.left and not root.left.left and not root.left.right 
    ? root.left.val 
    : sumOfLeftLeaves(root.left)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return (root.left.val if (root.left and not root.left.left and not root.left.right) \
            else self.sumOfLeftLeaves(root.left)) + (self.sumOfLeftLeaves(root.right))