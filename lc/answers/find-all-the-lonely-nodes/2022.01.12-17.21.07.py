class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []
        while stack:
            node, only_child = stack.pop()
            if only_child:
                res.append(node.val)
            has_one_child = (node.left and not node.right) or (node.right and not node.left)
            if node.left: stack.append((node.left, has_one_child))
            if node.right: stack.append((node.right, has_one_child))
        return res
