"""
after struggling to do it without extra memory... I just made this

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        def preorder(node):
            if not node: return []
            return [node] + preorder(node.left) + preorder(node.right)
        nodes = preorder(root)[::-1]
        res = nodes.pop()
        res.left = None
        curr = res
        while nodes:
            curr.right = nodes.pop()
            curr.left = None
            curr = curr.right
        return res


Now a stack solution because I read this could work
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        head = curr = root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            curr.left = None
            if curr != node:
                curr.right = node
                curr = curr.right
        return head

