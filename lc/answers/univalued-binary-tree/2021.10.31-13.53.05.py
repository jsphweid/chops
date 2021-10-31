class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def recurse(node, num):
            if node.val != num:
                return False
            left = recurse(node.left, num) if node.left else True
            right = recurse(node.right, num) if node.right else True
            return left and right
        return recurse(root, root.val)
