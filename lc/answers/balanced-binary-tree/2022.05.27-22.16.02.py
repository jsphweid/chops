class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def get_heights(node):
            nonlocal is_balanced
            if not node: return 0
            if not node.left and not node.right: return 1
            left = get_heights(node.left)
            right = get_heights(node.right)
            if abs(left - right) > 1:
                is_balanced = False
            return max(left, right) + 1

        get_heights(root)
        return is_balanced