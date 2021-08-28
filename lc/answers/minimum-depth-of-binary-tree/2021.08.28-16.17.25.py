"""
Like the other problems, I could easily re-use some logic and exit early once the first leaf is found. But
I kind of want to see if I can do this a different way.

Or I could combine various techniques I've used in the past to accomplish this for now -- for example, using
a queue and overriding values to mean depth, since we don't really care about the values here...

So the basic idea here is keeping a queue, adding new ones as I find them while descending. As soon as we find
a node with no children (leaf), we can exit with the depth of that leaf.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [TreeNode(1, root.left, root.right)]
        while len(queue):
            node = queue.pop(0)
            depth = node.val

            # if it's a leaf, exit with the depth!
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(TreeNode(depth + 1, node.left.left, node.left.right))
            if node.right:
                queue.append(TreeNode(depth + 1, node.right.left, node.right.right))

        # we shouldn't make it this far since every tree has a leaf

"""
worked the first time, although I feel like this approach is cheating a bit, since it overrides
the value of the node.
"""