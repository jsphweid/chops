# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depths = []
        self.populate_depths(root, 1, depths)
        return max(depths)

    def populate_depths(self, root: TreeNode, depth, depths):
        if not root.left and not root.right:
            depths.append(depth)
        if root.left:
            self.populate_depths(root.left, depth + 1, depths)
        if root.right:
            self.populate_depths(root.right, depth + 1, depths)
