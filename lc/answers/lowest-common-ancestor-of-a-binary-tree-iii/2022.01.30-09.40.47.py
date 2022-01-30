"""
===== Initial Thoughts =====
Hmm... I've never seen these where you have a connection to the parent.

I think I'll implement it without using the parent and then see if it can be written better using the parent.

Actually jokes on me. There is no root node! Now I understand why each node has a parent.

We could find the parent first.

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

That works but surely there's an easier way if we use the parent more strategically.
If p is the parent of q then while finding the parent of q we'll run across p, that's easy. And vice versa.

But what if they have the same parent which is not p or q? Then eventually they'll come across the same one.
Since vals are unique, we can just have a dict with the vals and can easily determine what the common one is.
"""

"""
# Definition for a Node.x 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = {}
        while p:
            if p.val == q.val:  # early exit if you run across it on the way up
                return p
            seen[p.val] = p
            p = p.parent
        while q:
            if q.val in seen:
                return seen[q.val]
            q = q.parent
