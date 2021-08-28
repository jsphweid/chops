"""
NOTE: root-to-leaf means to the end of each path. It went out of its way to tell me that a leaf
is a node with no children... that means it's pretty important.

I was using paper a lot in the beginning of this. I thought of a couple of different approaches for
this but they weren't immediately obvious when it came to thinking how it could be translated into
actual code.

One approach was to descend down the tree and accumulate sums somehow.
Another approach involved getting all routes to terminal ends then summing each to see if any
reached the sum.
But one that is starting to make more sense, is the one where we recurse down the tree, each time
making the targetSum arg less by the amount of the node it's on.

So it's going to involve calling `hasPathSum` on left/right if they exist. The exact rules are
not 100% clear to me, but that's the general idea.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # i.e. if is leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        new_value = targetSum - root.val
        return self.hasPathSum(root.left, new_value) or self.hasPathSum(root.right, new_value)


"""
This was definitely a good way to solve this as a first pass. I did fail once but only because I forgot self. again...
"""
