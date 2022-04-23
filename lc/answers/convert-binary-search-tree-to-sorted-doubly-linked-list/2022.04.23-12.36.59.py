"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""

recurse(8)
    recurse(5)
        recurse(2) -> 1,4
            recurse(1) -> 1,1
            recurse(3) -> 3,4
                r------
                recurse(4) -> 4,4
        recurse(7) -> 7,7

"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def recurse(node):
            if not node: return None, None
            l, h = recurse(node.left)
            ll, hh = recurse(node.right)
            node.left, node.right = h, ll
            if h: h.right = node
            if ll: ll.left = node
            lo, hi = l or h or node, hh or ll or node
            return lo, hi

        low, high = recurse(root)
        if low: low.left = high
        if high: high.right = low
        return low
