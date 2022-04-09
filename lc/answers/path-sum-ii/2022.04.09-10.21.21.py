"""
dfs(5, 22, [])
    dfs(4, 22, [5])
        dfs(11, 22, [5,4])
            dfs(7, 22, [5,4,11])
                dfs(None, 22, [5,4,11,7])
            dfs(2, 22, [5,4,11])
    dfs(8, 22, [5])

FAILED
this method leads to duplicates...

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res

    def dfs(self, node, target, path):
        if not node and sum(path) == target:
            self.res.append(path)
        if node:
            self.dfs(node.left, target, path + [node.val])
            self.dfs(node.right, target, path + [node.val])
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.target = targetSum
        self.dfs(root, root.val, [root.val])
        return self.res

    def dfs(self, node, total, path):
        if total == self.target and not node.left and not node.right:
            self.res.append(path)
        for c in [node.left, node.right]:
            if c: self.dfs(c, total + c.val, path + [c.val])
