"""
===== Initial Thoughts =====
can't we just put everything in a list and then make a new tree?

[3,1,5,7,2,3]
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.makeBst(self.get_inorder(root))

    def makeBst(self, lst):
        if not lst:
            return None
        mid = len(lst) // 2
        node = lst[mid]
        node.left = self.makeBst(lst[:mid])
        node.right = self.makeBst(lst[mid + 1:])
        return node

    def get_inorder(self, root):
        if not root:
            return []
        left = self.get_inorder(root.left)
        right = self.get_inorder(root.right)
        root.left = None
        root.right = None
        return left + [root] + right
