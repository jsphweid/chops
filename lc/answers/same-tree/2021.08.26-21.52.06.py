"""
My initial thoughts are we could compare the traversals of something like inorder to do a comparison.

The trick here is early exiting if possible. We could do an entire inorder traversal of each and compare
the results, but it's simply a waste of time to do the entire traversal when we know it fails before then.

Is there even a faster/better way of traversing a binary tree than the inorder traversal that I solved
in the last problem?

After considering it for 20 seconds or so, I think inorder traversal is a decent solution for this.
This focus now becomes on how do we do that in a clean/efficient way? We could use recursion again...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))

"""
Could this be solved iteratively?
"""