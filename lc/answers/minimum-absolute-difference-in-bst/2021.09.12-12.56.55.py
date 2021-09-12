"""
Let's see if we can do this recursively...

Unfortunately the first time I did this I incorrectly assumed only direct children would
count in the comparison even after successfully doing it using a queue before... :(

Here is that solution for reference:
        # if the child has at least one child, you can recurse
        diffs = []
        if root.left:
            diffs.append(abs(root.val - root.left.val))
            if root.left.left or root.left.right:
                diffs.append(self.getMinimumDifference(root.left))
        if root.right:
            diffs.append(abs(root.val - root.right.val))
            if root.right.left or root.right.right:
                diffs.append(self.getMinimumDifference(root.right))
        return min(diffs)

I'm going to see if I can adjust it to work with grandchildren.

So actually I'm not sure it's possible to only use recursion (returning diffs) because you need to be able
to do comparisons from child to grand-parent and with recursion you're destroying the original numbers making
that cross-generational comparison impossible. You could use recursion to get all the nodes though. I guess
that's what I'll do for now.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_inorder_values(self, root):
        if not root:
            return []
        return self.get_inorder_values(root.left) + [root.val] + self.get_inorder_values(root.right)


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = self.get_inorder_values(root)
        # vals.sort()
        diffs = []
        for i in range(1, len(vals)):
            diffs.append(vals[i] - vals[i - 1])
        return min(diffs)