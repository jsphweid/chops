class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.target = targetSum
        self.res = []
        self.dfs(root, root.val, [root.val])
        return self.res

    def dfs(self, node, total, path):
        if not node.left and not node.right and total == self.target:
            self.res.append(path)
        else:
            for c in [node.left, node.right]:
                if c:
                    self.dfs(c, total + c.val, path + [c.val])