"""
===== Initial Thoughts =====
We could get all the values using inorder traversal. Since it's a BST, it's sorted already. Then we can do one
scan to find the min difference.

Since it's BST, I _think_ the minimal distance has to be between the parent and child. IE, it can't be between
two distance nodes. 

=== Implemented Approach ===
Let's solve using recursion. We should be able to use the main function definition for everything. We can't get too
deep in the tree though. There always must be a parent/child relationship for this work since that is where
the comparison happens. If we have a node with no children, then how can we find the difference? Let's not put
ourselves in that position. The constraints indicate that there are at least two nodes, indicating at least one child.

~~Complexity Analysis
Time - O(n)? Not sure how you do time complexity on a tree
Space - O(1) as we're not storing anything significant

ACTUALLY I FAILED THE FIRST TIME BECAUSE THIS APPROACH DOESN'T WORK:
        nums_to_compare = []
        if root.left:
            nums_to_compare.append(root.val - root.left.val)
            if root.left.left or root.left.right:
                nums_to_compare.append(self.minDiffInBST(root.left))
        if root.right:
            nums_to_compare.append(root.right.val - root.val)
            if root.right.left or root.right.right:
                nums_to_compare.append(self.minDiffInBST(root.right))
        return min(nums_to_compare)

It fails because minimum differences can happen outside parent/child relationships. I failed to consider this.

Let's do a more standard approach... 

~~Complexity Analysis
Time - O(n)? Not sure how you do time complexity on a tree
Space - O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        lst = inorder(root)
        return min([b - a for a, b in zip(lst, lst[1:])])