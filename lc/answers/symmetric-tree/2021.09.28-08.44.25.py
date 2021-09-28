"""
=== Implemented Approach ===
iterative, get one layer at a time, confirm it's symmetry
we can do this with two lists. One to process current nodes and one to put new nodes into.
Once the current nodes list is empty, we replace it with the other one -- that's when a new layer is formed
so in that step we would also verify it's symmetry


~~Complexity Analysis
Time - O(n) where n is the number of nodes in the tree
Space - O(n) -- we need a single layer, the last as max, but it goes one past (the Nones), so an extra layer 
    is actually the number of nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        buffer = []
        queue = [root]
        while len(buffer) or len(queue):
            if len(queue):
                # we're in gathering mode
                top = queue.pop(0)
                if top: 
                    buffer.append(top.left)
                    buffer.append(top.right)
            else:
                # we're in assertion/reset mode
                vals = list(map(lambda x: x.val if x else None, buffer))
                if vals != vals[::-1]:
                    return False
                queue = buffer
                buffer = []
        return True
