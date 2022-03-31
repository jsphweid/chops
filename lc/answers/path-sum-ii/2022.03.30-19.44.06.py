"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, 0, [], targetSum)
        return self.res

    def dfs(self, node, total, path, target):
        total += node.val
        if not node.left and not node.right and target == total:
            self.res.append(path + [node.val])
        else:
            if node.left: self.dfs(node.left, total, path + [node.val], target)
            if node.right: self.dfs(node.right, total, path + [node.val], target)

or......
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.dfs(root, root.val, [root.val], targetSum)
        return self.res

    def dfs(self, node, total, path, target):
        if not node.left and not node.right and target == total:
            self.res.append(path)
        else:
            for n in [node.left, node.right]:
                if n:
                    self.dfs(n, total + n.val, path + [n.val], target)
