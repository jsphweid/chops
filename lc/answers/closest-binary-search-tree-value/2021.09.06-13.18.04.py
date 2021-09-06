"""
Should be able to keep track of the "closest" value as we traverse. If we encounter a closer
one, return that.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # says optional, but num nodes is minimal 1... so I think it's a lie
        closest = root.val
        distance = abs(closest - target)

        while True:
            if root.val == target:
                return root.val
            this_distance = abs(root.val - target)
            if this_distance < distance:
                distance = this_distance
                closest = root.val
            if root.left and target < root.val:
                root = root.left
            elif root.right and target > root.val:
                root = root.right
            else:
                break

        return closest

