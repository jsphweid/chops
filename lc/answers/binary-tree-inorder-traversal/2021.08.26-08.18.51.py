"""
My first impression is that I don't understand this at all.

What exactly is "inorder" traversal. I'm trying to understand the images before I
google it.

Maybe it's a left-right traversal? i.e. Does all the lefts, then does the rights.

The thumbs up to thumbs down ratio seems to indicate this is ridiculously easy
I also read that `Follow up: Recursive solution is trivial, could you do it iteratively?`

Example 2/3 are the easy cases to handle.

Since I feel like the examples provided do not a conclusive enough description
of the problem, I'm going to google "inorder".

"inorder" is left-root-right
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ## ON FUTHER INSPECTION, THIS SEEMS TO BE UNNECESSARY
        # if not root.left and not root.right:
        #     return [root.val]

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

#   failed the first time just because I forgot `self.`


        