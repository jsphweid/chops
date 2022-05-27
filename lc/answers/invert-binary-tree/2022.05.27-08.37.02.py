"""
fn(4)
    left => fn(7)
        left => fn(9)
            left => None
            right => None
        right => fn(6)
    right => fn(2)

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            left, right = root.left, root.right
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        return root