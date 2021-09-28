"""
===== Initial Thoughts =====
if we go top down (breath first search) and process each row... then the first
time we encounter a node with no children, that is the depth

=== Implemented Approach ===
if no node, return 0
else start the bfs using a queue, keep a second list that fills the children
then switch it over and increment some depth var. Once we've encountered a node
with no children, just return the current depth.

~~Complexity Analysis
Time - O(n)
Space - O(n/2)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        buffer = []
        queue = [root]
        while len(buffer) or len(queue):
            if len(queue):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left: buffer.append(node.left)
                if node.right: buffer.append(node.right)
            else:
                depth += 1
                queue = buffer
                buffer = []