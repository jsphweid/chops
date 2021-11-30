"""
=== Brute Force Approach ===
We can do dfs with some path and evaluate the path at every turn checking to see if the last
is the max of the path. But how do we make that efficient?

=== Implemented Approach ===
Actually we may not need a path but the max number that has been seen on the path. When we evaluate
a node, we check to see if the max of that path is greater than the node in question. If it's greater
than it's a bad node. But same or less would mean it's a good node.

~~Complexity Analysis
Time - O(n) where n is the number of nodes
Space - 

tracing

count = 4
dfs(3, -1000) # NOTE: failed first time because this has to be -10000...
    dfs(1, 3)
        dfs(3, 3)
    dfs(4, 3)
        dfs(1, 4)
        dfs(5, 4)

seems to work

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_num=-10000):
            nonlocal count
            if node.val >= max_num: count += 1
            if node.left: dfs(node.left, max(max_num, node.val))
            if node.right: dfs(node.right, max(max_num, node.val))
        dfs(root)
        return count

refactoring... how can we get this down to one function call...?

goodNodes(3, -10000, 0) => 4
    current = 1
    left = goodNodes(1, 3, 0) => 1
        current = 0
        left = goodNodes(3, 3, 0) => 1
            current = 1
            left => 0
            right => 0
        right = goodNodes(None, 3, 0) => 0
    right = goodNodes(4, 3, 0) => 2
        current = 1
        left = goodNodes(1, 4, 0) => 0
            current = 0
            left => 0
            right => 0
        right = goodNodes(5, 4, 0) => 1
            current = 1
            left => 0
            right => 0

the best?
class Solution:
    def goodNodes(self, root: TreeNode, max_num=-10000) -> int:
        if not root: return 0
        current = 1 if root.val >= max_num else 0
        left = self.goodNodes(root.left, max(max_num, root.val))
        right = self.goodNodes(root.right, max(max_num, root.val))
        return current + left + right

one liner...
    def goodNodes(self, root: TreeNode, a=-10000) -> int:
        return (root.val >= a) + self.goodNodes(root.left, max(a, root.val)) + self.goodNodes(root.right, max(a, root.val)) if root else 0
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_num=-10000) -> int:
        if not root: return 0
        current = 1 if root.val >= max_num else 0
        left = self.goodNodes(root.left, max(max_num, root.val))
        right = self.goodNodes(root.right, max(max_num, root.val))
        return current + left + right
