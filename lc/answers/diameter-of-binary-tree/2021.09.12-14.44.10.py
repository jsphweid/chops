"""
max length between any two nodes

for every node, we need to append max left + max right

I don't think this can be done with 'perfect recursion' (1 function) but it can probably
be done with helper recursive functions...

but we wouldn't want to trace through a path multiple times... not sure how to avoid that for now
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDepth(self, root, depth=0):
        if not root:
            return 0
        if not root.left and not root.right:
            return depth
        return max(self.getMaxDepth(root.left, depth + 1), self.getMaxDepth(root.right, depth + 1))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        farthest = 0
        while len(queue):
            node = queue.pop(0)
            reach = self.getMaxDepth(node.left, 1) + self.getMaxDepth(node.right, 1)
            farthest = max(farthest, reach)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return farthest
