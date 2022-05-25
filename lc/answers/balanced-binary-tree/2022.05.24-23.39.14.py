class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node: return 0
            left_height = 1 + dfs(node.left)
            right_height = 1 + dfs(node.right)
            if abs(left_height - right_height) > 1:
                res = False
            return max(left_height, right_height)
        dfs(root)
        return res