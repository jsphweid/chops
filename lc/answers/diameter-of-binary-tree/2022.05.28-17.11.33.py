"""
===== Initial Thoughts =====
just get length of each side and bubble it up. Compare the
left+right at every node as you go up to some global max

FAILED initially
dfs(1)
    dfs(2) -> 1
    dfs(N) -> 0
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            nonlocal longest

            if not node:
                return 0
            if not node.left and not node.right:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            longest = max(longest, left + right)
            return max(left, right) + 1

        dfs(root)
        return longest