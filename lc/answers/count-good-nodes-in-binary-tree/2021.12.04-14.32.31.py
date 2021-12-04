class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res, stack = 0, [(root, root.val)]
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val: res += 1
            if node.left: stack.append((node.left, max(max_val, node.val)))
            if node.right: stack.append((node.right, max(max_val, node.val)))
        return res
