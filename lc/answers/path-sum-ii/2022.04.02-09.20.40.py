class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, targetSum, root.val, [root.val])
        return self.res

    def dfs(self, node, target, curr, path):
        if not node.left and not node.right and curr == target:
            self.res.append(path)
        for c in [node.left, node.right]:
            if c:
                self.dfs(c, target, curr + c.val, path + [c.val])
