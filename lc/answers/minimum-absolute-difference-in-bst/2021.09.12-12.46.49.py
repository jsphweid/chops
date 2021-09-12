"""
we could traverse all nodes extracting values
we could sort that list of values
we could translate that into a vector of absolute differences and return min value
Seems fair for a first pass...
I think this could be solved recursively as well...?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        q = [root]
        while len(q):
            node = q.pop(0)
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        vals.sort()
        diffs = []
        # there are at least 2 nodes... so we don't need any safety mechanism
        for i in range(1, len(vals)):
            diffs.append(vals[i] - vals[i - 1])
        return min(diffs)
