class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if node is p or node is q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            return node if left and right else left or right
        return dfs(root)
