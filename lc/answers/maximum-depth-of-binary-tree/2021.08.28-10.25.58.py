"""
This solution involves overriding node values with the depth. The trick here
is that the first node must have a value of one -- since there this tree is a
one-way with no ref to parents, I think the only way we can know if we're on the first
node is to intercept it and pass it to an inner function. There _might_ be another
way of doing this.

There also might be some difficulties with the max function at the end. If we
use an inner function, we shouldn't have too many problems with this though.
This is because we're basically doing inorder traversal to get the depths from
left to right.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def _get_depths(r: Optional[TreeNode]):
            if not r:
                return []
            next_val = r.val + 1
            left_node = TreeNode(next_val, r.left.left, r.left.right) if r.left else None
            right_node = TreeNode(next_val, r.right.left, r.right.right) if r.right else None
            return _get_depths(left_node) + [r.val] + _get_depths(right_node)

        return max(_get_depths(TreeNode(1, root.left, root.right)))
        