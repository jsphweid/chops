"""
So this differs form inorder. I think the only difference we need to make
is instead of left, center, right... do center, left, right??

That doesn't seem very useful though... I might need to look up a few things
to clarify exactly what preorder means because the examples aren't detailed
enough to make it obvious to me.

I found an image and it seems like my suspicions are correct.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)