"""
===== Initial Thoughts =====
so we have to find the node first... then look through its parent
it's the next largest value I believe?

Finding the node is logn because it's a BST. Finding the next should
also be logn. This is hard because we don't have a connection
to the parent...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
find(5)
"""

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        lst = [root]
        # [5n, 6n]
        while root is not p:
            if p.val > root.val:
                root = root.right
            else:
                root = root.left
            lst.append(root)
        res = self.find_next_largest(lst[-1])
        if res:
            return res
        if not res:
            for i in range(len(lst) - 1, -1, -1):
                if lst[i].val > p.val:
                    return lst[i]

    def find_next_largest(self, node):
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        return None
