"""
===== Initial Thoughts =====
Hmm... I've never seen these where you have a connection to the parent.

I think I'll implement it without using the parent and then see if it can be written better using the parent.

Actually jokes on me. There is no root node! Now I understand why each node has a parent.

We could find the parent first.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

def find_parent(node):
    return find_parent(node.parent) if node.parent else node

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = find_parent(p)

        def recurse(node):
            if node in [None, p, q]:
                return node
            left = recurse(node.left)
            right = recurse(node.right)
            return node if right and left else right or left

        return recurse(root)