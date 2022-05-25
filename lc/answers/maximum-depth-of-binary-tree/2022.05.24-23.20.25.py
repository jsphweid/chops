class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if root and not root.left and not root.right: return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))