""" 
I can't imagine this is that different that binary max depth search...
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node', depth=1) -> int:
        if not root:
            return 0
        if not len(root.children):
            return depth
        return max([self.maxDepth(c, depth + 1) for c in root.children])