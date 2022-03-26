"""
===== Initial Thoughts =====
didn't realize until reading the discussions that this can be a lot simpler

the idea is we can always take one path to find the result
"""
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = None
        while root:
            if root.val > p.val: # too big, go left
                res = root
                root = root.left
            else:
                root = root.right
        return res