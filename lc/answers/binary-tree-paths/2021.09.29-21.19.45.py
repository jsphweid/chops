"""
=== Implemented Approach ===
have an inner recursive fn that can access some global list. it also takes in a list
if no child nodes, append list arg to global list
if there are children, recurse calling fn with new list that includes current, ignore the None side
in single child situations

finally, with the ending lists, just map over that global list converting each into the strings

I'm not immediately sure how to model complexity for this...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        def recurse(node, accum):
            if not node.left and not node.right:
                all_paths.append(accum)
            else:
                if node.left: recurse(node.left, accum + [str(node.left.val)])
                if node.right: recurse(node.right, accum + [str(node.right.val)])
        recurse(root, [str(root.val)])
        return list(map(lambda l: "->".join(l), all_paths))
