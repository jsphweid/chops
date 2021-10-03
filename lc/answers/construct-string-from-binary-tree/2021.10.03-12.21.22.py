"""
[1,2,3,4]
"1(2(4)())(3)"
"1(2(4))(3)" - correct

[1,2,3,null,4]
"1(2(4))(3)"
"1(2()(4))(3)" - correct
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        string = str(root.val)
        if not root.left and not root.right: return string
        string += f"({self.tree2str(root.left)})"
        if root.right: string += f"({self.tree2str(root.right)})"
        return string