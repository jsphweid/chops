class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return []
            return dfs(node.left) + [node] + dfs(node.right)
        nodes = dfs(root)
        first = None
        last = None
        while len(nodes):
            node = nodes.pop(0)
            node.left = None
            if not first: 
                first = last = node
                continue
            last.right = node
            last = node
        return first