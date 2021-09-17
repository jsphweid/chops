"""
This question seems a bit odd because the rules make it seem like numbers only get bigger as the tree
gets deeper... If that's the case then the minimum is always the root node. And the second minimum is
always the child that's not the smallest.

But the second example shows that apparently both children can be the same size...

A naive solution here could simply traverse the whole tree, put everything in a sorted list, and pick the
second smallest number. But that's not really taking advantage of the structure.

The tree could have sooo many duplicates and the "next smallest" is at the very bottom while other appealing
choices are near the top on other leaves. You could stop once you find the next obvious value (if root is 2,
then stop at 3.). That'd help us early exit but for the most part we kinda need to traverse the entire tree
until that obvious answer exists (or there's no more tree to search).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals = []
        nodes = [root]
        for node in nodes:
            if root.val + 1 == node.val:
                return node.val
            vals.append(node.val)
            if node.left: # if it has one, it has both -- according to the problem
                nodes.extend([node.left, node.right])
        vals.sort()
        for val in vals:
            if val != root.val:  # the first one that isn't the lowest has to be it since we sorted
                return val
        return -1