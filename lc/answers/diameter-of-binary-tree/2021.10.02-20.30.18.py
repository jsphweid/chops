# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = 0
        def find_max_depth(node):
            nonlocal longest_diameter
            if not node.left and not node.right: return 0
            left_len = 1 + find_max_depth(node.left) if node.left else 0
            right_len = 1 + find_max_depth(node.right) if node.right else 0
            longest_diameter = max(longest_diameter, left_len + right_len)
            return max(left_len, right_len)
        find_max_depth(root)
        return longest_diameter

