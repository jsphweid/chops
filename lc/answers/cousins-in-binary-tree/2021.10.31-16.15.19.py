class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False
        queue = [root]
        next_row = set()
        while len(queue):
            node = queue.pop(0)
            if node.left: next_row.add(node.left)
            if node.right: next_row.add(node.right)
            if node.left and node.right:
                if set([node.left.val, node.right.val]) == {x, y}:
                    return False
            if not len(queue):
                vals = {n.val for n in next_row}
                if x in vals and y in vals: return True
                queue.extend(list(next_row))
                next_row = set()
        return False
