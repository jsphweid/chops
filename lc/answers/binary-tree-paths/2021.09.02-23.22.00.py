"""
Ok I looked at some help online to get started... Turns out it is pretty normal to create a 
different function -- the one that you're going to use to recurse...
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(root, string, lst):
    string += str(root.val)
    if root.left:
        recurse(root.left, f"{string}->", lst)
    if root.right:
        recurse(root.right, f"{string}->", lst)
    if not root.left and not root.right:
        lst.append(string)


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        recurse(root, "", result)
        return result