class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def recurse(node, n):
            nonlocal total
            new_num = (n << 1) | node.val
            if not node.left and not node.right:
                total += new_num
            if node.left: recurse(node.left, new_num)
            if node.right: recurse(node.right, new_num)
        recurse(root, 0)
        return total