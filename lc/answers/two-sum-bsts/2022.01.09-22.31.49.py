"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def get_vals(root):
            if not root: return []
            return [root.val] + get_vals(root.left) + get_vals(root.right)
        seen = set(get_vals(root1))
        for num in get_vals(root2):
            compliment = target - num
            if compliment in seen:
                return True
        return False










