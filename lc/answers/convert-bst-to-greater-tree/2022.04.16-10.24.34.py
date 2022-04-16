"""
===== Initial Thoughts =====
should just be able to do reversed inorder and keep a running sum
which is used to modify node values

def inorder(root):
    if not root: return []
    return inorder(root.left) + root + inorder(root.right)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = self.trav(root)
        total = 0
        for node in nodes:
            nxt = node.val + total
            node.val, total = nxt, nxt
        return root

    def trav(self, root):
        if not root: return []
        return self.trav(root.right) + [root] + self.trav(root.left)

But can we do it with O(1) space and a single pass?
"""

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        self.trav(root)
        return root

    def trav(self, node):
        if node:
            self.trav(node.right)
            nxt = node.val + self.total
            node.val, self.total = nxt, nxt
            self.trav(node.left)
