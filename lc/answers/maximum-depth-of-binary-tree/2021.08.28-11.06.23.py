# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        return max([self.maxDepth(root.left, depth + 1), depth, self.maxDepth(root.right, depth + 1)])

    """
    Pre-submit: let's go through this with their example:
    works for null root case.
    This is a little tricky to think about but I think this could work
    The weird think is that the depth of the null node is what determines the depth
    but since we start at 0 instead of 1, it should be fine -- it's less code this way
    although maybe a little unintuitive.

    if not root:
        return depth
    return max([maxDepth(root.left, depth + 1), depth, maxDepth(root.right, depth + 1)])

    Submission failed. I might want to think about this a little more.
    Actually it failed just because I forgot `self.`... again FML
    """